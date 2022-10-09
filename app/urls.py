from django.urls import path
from. import views

urlpatterns=[

    path('home',views.index,name='index'),
    path('events',views.events,name='events'),
    path('sermons',views.sermons,name='sermons'),
    path('location',views.location,name='location'),
    


]