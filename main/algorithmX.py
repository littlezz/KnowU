from random import randint
from main.models import Article

__author__ = 'zz'



#
# /**
# *
# *----------Dragon be here!----------/
# * 　　　┏┓　　　┏┓
# * 　　┏┛┻━━━┛┻┓
# * 　　┃　　　　　　　┃
# * 　　┃　　　━　　　┃
# * 　　┃　┳┛　┗┳　┃
# * 　　┃　　　　　　　┃
# * 　　┃　　　┻　　　┃
# * 　　┃　　　　　　　┃
# * 　　┗━┓　　　┏━┛
# * 　　　　┃　　　┃神兽保佑
# * 　　　　┃　　　┃代码无BUG！
# * 　　　　┃　　　┗━━━┓
# * 　　　　┃　　　　　　　┣┓
# * 　　　　┃　　　　　　　┏┛
# * 　　　　┗┓┓┏━┳┓┏┛
# * 　　　　　┃┫┫　┃┫┫
# * 　　　　　┗┻┛　┗┻┛
# * ━━━━━━神兽出没━━━━━━
# */


def AlgorithmX(user):
    """

    :param user:  User model
    :return: a single Article instance
    """
    #TODO: improve performance!
    query = Article.objects.filter(tags=user.userprofile.tags.all())

    if not query.exists():
        query = Article.objects.all()

    total = query.count()
    random_num = randint(0, total-1)
    ret_article = query[random_num]

    return ret_article