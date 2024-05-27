from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:question_id>/', views.update, name='update'),
    path('delete/<int:question_id>/', views.delete, name='delete'),
]
