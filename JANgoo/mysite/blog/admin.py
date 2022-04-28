from django.contrib import admin
from .models import Post

# Register your models here.
mymodels = [Post]
admin.site.register(mymodels)