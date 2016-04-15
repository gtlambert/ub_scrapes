from django.shortcuts import render

from .models import Category, Review


def home(request):
    return render(request, 'demo_data/home.html',
                  {'categories': Category.objects.all()})


def category_page(request, category_num):
    category = Category.objects.get(num=category_num)
    reviews = Review.objects.filter(category=category)
    return render(request,
                  'demo_data/category.html',
                  {'category': category,
                   'reviews': reviews})


def review_page(request, category_num, review_num):
    # category = Category.objects.get(num=category_num)
    review = Review.objects.get(num=review_num, category=category_num)
    return render(request,
                  'demo_data/review.html',
                  {'review': review})
