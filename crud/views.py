from django.shortcuts import render
from django.http import HttpResponse


def blog(request):
   return render(request, 'blog.html')


def blog_details(request):
    return render(request, 'blog_details.html')


def checkout(request):
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def shop_details(request):
    return render(request, 'shop_details.html')


def shop_grid(request):
    return render(request, 'insurance.html')


def shoping_card(request):
    return render(request, 'packages.html')

