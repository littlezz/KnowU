from django.contrib.auth.models import User
from django.db import models
# Create your models here.




class Tag(models.Model):

    label = models.CharField(max_length=20)

    def __str__(self):
        return self.label



class Article(models.Model):

    tags = models.ManyToManyField(Tag)
    headline = models.CharField(max_length=30)
    content = models.TextField()
    favour = models.ManyToManyField(User, related_name='+')


    def how_many_favour(self):
        return self.favour.count()

    def how_many_booked(self):
        return self.user_book.count()

    def __str__(self):
        return self.headline


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tags = models.ManyToManyField(Tag, blank=True)
    article_books = models.ManyToManyField(Article,related_name='user_book', through='BookArticleMembership', blank=True)
    article_history = models.ManyToManyField(Article, related_name='user_history', blank=True)

    def __str__(self):
        return self.user.username





class BookArticleMembership(models.Model):
    userinfo = models.ForeignKey(UserProfile)
    article = models.ForeignKey(Article)
    join_date = models.DateField(auto_now_add=True)

