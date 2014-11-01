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
    query = Article.objects.filter(tags=user.userprofile.tags.all())

    total = query.count()
    print('test!', total)
    if total == 0:
        query = Article.objects.all()
        total = Article.objects.count()

    print('finall', total)
    random_num = randint(0, total-1)

    return query[random_num]