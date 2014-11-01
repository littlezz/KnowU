from django.db import models

# Create your models here.
from django import forms

class TemTag(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class TemArticle(models.Model):
    headline = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(TemTag, blank=True)

    def __str__(self):
        return self.headline

class Xml(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    tags = models.ManyToManyField(TemTag, blank=True)

    def __str__(self):
        return self.name


class CheckCommitForm(forms.Form):
    value = forms.CharField(max_length=10,initial='ok',help_text='我已经确认所有文章可以提交,提交之后这些临时文章将会被清除.')