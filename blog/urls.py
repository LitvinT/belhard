from django.urls import path

from .views import contact, blog_list, post_detail, about

urlpatterns = [
    path('', blog_list, name='blog_posts'),
    path('contact/', contact, name='blog_contact'),
    path('about/', about, name='blog_about'),
    path('<slug:post_slug>/', post_detail, name='blog_post')
]