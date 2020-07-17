from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('eventdetails<int:event_id>', views.eventdetails, name='eventdetails'),
    path('eventslist', views.eventslist),
    path('newevent', views.newevent),
    path('navigator', views.navigator),
    path('contact', views.contact),
    path('newmenu', views.newmenu),
    path('menudetails<int:menu_id>', views.menudetails),
    path('menulist', views.menulist),
    path('messages', views.messages),
    path('book_event', views.book_event, name='book'),
    path('book_menu', views.book_menu, name='book_menu'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('message', views.message_in, name='message')
]
