from django.urls import path
from .views import *

urlpatterns = [
    path('whyus/',WhyUsView.as_view(),name='whyus'),
    path('partners/',PartnersView.as_view(),name='partners'),
    path('laptop/',LaptopsView.as_view(),name='laptops'),
    path('faq/',FAQView.as_view(),name='faq'),
    path('about/',AboutView.as_view(),name='about'),
    path('program/',ProgramView.as_view(),name='program'),
]