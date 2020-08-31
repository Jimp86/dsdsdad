from django.urls import path
from index.views import index, home
from apps.users.views import Login
urlpatterns = [
    path('', index, name="index"),
    path('home', home, name="home"),
    path('login/', Login.as_view(), name="login"),

]