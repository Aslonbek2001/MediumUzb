from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),
    # path('pricing/', views.pricing, name='pricing'),
    # path('blog/', views.blog, name='blog'),
    # path('blog-details/', views.blog_details, name='blog-details'),
    # path('faq/', views.faq, name='faq'),
    # path('404/', views.error, name='404'),
    # path('coming-soon/', views.coming_soon, name='coming-soon'),
    # path('privacy-policy/', views.privacy_policy, name='privacy-policy'),
    # path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),
    # path('login/', views.login, name='login'),
]