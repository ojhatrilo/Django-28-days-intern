from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="hello"),
    path('time/', views.date, name="date")
]
