from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def blog_home(request):
    return render(request, 'blog-home.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        sub = request.POST['subject']
        msg = request.POST['message']
        data = Contact.objects.create(
            name=name,
            email=email,
            subject=sub,
            message=msg
        )
        data.save()
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def price(request):
    return render(request, 'price.html')
