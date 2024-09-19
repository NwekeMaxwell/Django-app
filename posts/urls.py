from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    # path("<id>/", views.post), #this path allows the id to be any type of data type
    path("<int:id>/", views.post, name='post') #this path allows the id to be sprcified type of data type, the name parameter is used for redirect
]