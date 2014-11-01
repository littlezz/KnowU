from django.contrib import admin
from .models import Tag, Article, UserProfile, BookArticleMembership

# Register your models here.

class TagArticleShipInline(admin.TabularInline):
    model = Article.tags.through
    extra = 3


class TagAdmin(admin.ModelAdmin):
    exclude = ['users',]

admin.site.register(Tag, TagAdmin)


class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagArticleShipInline]
    exclude = ['tags', 'favour']
    list_display = ['headline', 'how_many_favour']
admin.site.register(Article, ArticleAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(BookArticleMembership)