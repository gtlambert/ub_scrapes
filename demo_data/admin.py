from django.contrib import admin

from .models import Category, Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['num']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['num', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
