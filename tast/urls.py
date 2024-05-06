from django.urls import path
from .views import tex

     

urlpatterns = [
    path('te',tex,name='temp'),

]