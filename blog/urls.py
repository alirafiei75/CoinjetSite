from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog_view, name='blog'),
    path('single', single_view, name='single')
]