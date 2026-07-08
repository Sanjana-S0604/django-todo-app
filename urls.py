from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('completed/',completed,name='completed'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('update/<int:pk>',update,name='update'),
    
    path('hcomplete/<int:pk>',hcomplete,name='hcomplete'),
    path('hdelete/<int:pk>',hdelete,name='hdelete'),
    path('hcomplete_all/',hcomplete_all,name='hcomplete_all'),
    path('hdelete_all/',hdelete_all,name='hdelete_all'),

    path('crestore/<int:pk>',crestore,name='crestore'),
    path('cdelete/<int:pk>',cdelete,name='cdelete'),
    path('crestore_all/',crestore_all,name='crestore_all'),
    path('cdelete_all/',cdelete_all,name='cdelete_all'),

    path('trestore/<int:pk>',trestore,name='trestore'),
    path('trestore_all/',trestore_all,name='trestore_all'),
    path('tdelete/<int:pk>',tdelete,name='tdelete'),
    path('tdelete_all/',tdelete_all,name='tdelete_all')


    

]