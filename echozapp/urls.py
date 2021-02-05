from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('What.html/', views.about, name='What'),
    path('blog-single.html/', views.blogSingle, name='blog-single'),
    path('categories.html/', views.categories, name='categories'),
    path('contact.html/', views.contact, name='contact'),
]