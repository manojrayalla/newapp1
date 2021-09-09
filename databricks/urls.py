# howdy/urls.py
from django.urls import path
from databricks import views


urlpatterns = [
    path('', views.form_name_view, name ='forms'),
    path('response', views.response_view, name ='responseview'),
]