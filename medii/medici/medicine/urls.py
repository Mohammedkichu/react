
from django.urls import path
from . import views
from .views import delete



urlpatterns = [
    path('',views.signuppage, name="signup"),
    path('login/',views.loginpage, name="login"),
    path('home/',views.homepage, name="home"),
    path('search/',views.search, name="search"),
    path('logout/',views.logoutpage, name="logout"),
    path('create/',views.create, name="create"),
    path('delete/<int:id>/',views.delete, name="delete"),
    path('<int:id>/',views.update, name="update"),
  
]