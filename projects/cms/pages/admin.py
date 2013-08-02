from models import *
from django.contrib import admin

admin.ModelAdmin.list_per_page = 25


class CategoryAdmin(admin.ModelAdmin):
    #
    fields = ['name', 'parent', 'allow_replies']
    #
    list_display = ('id', 'name', 'parent')
    #
    search_fields = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class PageAdmin(admin.ModelAdmin):
    #
    fields = ['category', 'title', 'content']
    #
    list_display = ('id', 'title')
    #
    search_fields = ('title', 'category')


admin.site.register(Page, PageAdmin)
