from django.urls import path
from App_Posts import views

app_name = 'App_Posts'


urlpatterns = [
    path('home/', views.Home_View, name="home"),
    path('like/<pk>/', views.Like_View, name="like"),
    path('unlike/<pk>/', views.Unlike_View, name="unlike"),
]
