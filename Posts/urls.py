from django.urls import path
from .views import demo

urlpatterns = [
    path('',demo.as_view(),name='demo')
]
