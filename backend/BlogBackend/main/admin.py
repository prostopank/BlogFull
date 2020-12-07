from django.contrib import admin

from main.models import Article, Comments, FavoriteArticle

admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(FavoriteArticle)
