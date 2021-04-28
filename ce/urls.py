from django.conf.urls import url
from ce import views
from django.urls import path

urlpatterns = [
    path('ce/<int:id>/', views.index),
]
