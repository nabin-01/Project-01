from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('blog-home/', blog_home, name='blog_home'),
    path('blog-single/', blog_single, name='blog_single'),
    path('contact/', Contact, name='contact'),
    path('elements/', elements, name='elements'),
    path('portfolio/', portfolio, name='portfolio'),
    path('price/', price, name='price'),
]
