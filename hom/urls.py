from django.urls import path
from .views import home_pag,sing_pag,log_pag,profil_pag,nuse_pag,lockhome_pag,user_logout,\
profil_updt,profil_updt_to
     

urlpatterns = [
    path('',home_pag,name='home'),
    path('pr',profil_pag,name='prof'),
    path('nu',nuse_pag,name='nuse'),
    path('si',sing_pag,name='sing'),
    path('lo',log_pag,name='log'),
    path('kho',lockhome_pag,name='lockhome'),
    path('use',user_logout,name='user_log'),
    path('pro',profil_updt,name='profl'),
    path('pto',profil_updt_to,name='profl_to'),
 
]