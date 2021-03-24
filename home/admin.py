from django.contrib import admin
from .models import *
# Register your models here.
# to register and display in admin panel
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Project)
admin.site.register(Brand)
