from django.urls import path
from . import views

app_name = 'expenses'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
