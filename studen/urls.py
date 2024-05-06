from django.urls import path
from .views import veo,add_casterm,updete_vew 

urlpatterns = [
    path('ve',veo,name='veo'),
    path('add',add_casterm ,name='add'),
    path('upde/<int:pk>/',updete_vew ,name='upde'),
]