from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculator),
    path('result', views.result )
]