from django.urls import path
from sample_app import views


app_name = 'sample_app'
urlpatterns = [
    path('/', views.test, name='test'), 
]