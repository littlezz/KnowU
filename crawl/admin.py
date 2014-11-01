from django.contrib import admin

# Register your models here.
from . import models

class TemArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.TemArticle, TemArticleAdmin)

admin.site.register(models.TemTag)
admin.site.register(models.Xml)