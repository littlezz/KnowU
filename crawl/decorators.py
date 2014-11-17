__author__ = 'zz'

from functools import wraps
from requests import Timeout, ConnectionError
import socket
import logging


timeouts = (Timeout, socket.timeout, ConnectionError)


def retry_connect(retry_times, timeout):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try_times = 0
            while True:
                try:
                    ret = func(*args, timeout=timeout, **kwargs)

                    if ret.status_code != 200:
                        # error.connect_not_ok(ret.url, ret.status_code, ret.reason)
                        # raise Timeout
                        logging.warning('%s is %s', ret.url, ret.status_code)
                        if ret.status_code == 404:
                            raise Timeout

                except timeouts:

                    try_times += 1
                else:
                    return ret

                if try_times >= retry_times:
                    raise Timeout

        return wrapper
    return decorator


def lazyproperty(func):
    name = '_property_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            val = func(self)
            setattr(self, name, val)
            return val

    return lazy


def loop(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            ret = func(*args, **kwargs)
            if ret:
                break
    return wrapper


def resolve_timeout(replace_value):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except timeouts as e:
                return replace_value
        return wrapper
    return decorator