from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    views = dict()
    views['feedbacks'] = Review.objects.all()
    # views['projects'] = Project.objects.all()
    views['brands'] = Brand.objects.all()
    return render(request, 'index.html', views)


def about(request):
    views = dict()
    views['feedbacks'] = Review.objects.all()
    return render(request, 'about.html', views)


def services(request):
    return render(request, 'services.html')


def blog_home(request):
    return render(request, 'blog-home.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def contact(request):
    # 'POST' means form is being submitted
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
        # check entered user data is correct or not by python validators
        # saves form data to DB
        data.save()
        views = dict()
        views['message'] = 'The form is successfully submitted!'
        return render(request, 'contact.html', views)
    # if response it render it looks for a HTML
    return render(request, 'contact.html')


def elements(request):
    return render(request, 'elements.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def price(request):
    return render(request, 'price.html')
