
from django.urls import path
from . import views

urlpatterns = [

    path('home/',views.homepage, name="home"),
    path('add/',views.addpage, name="create"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('',views.signup,name="signup"),
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout, name="logout"),
    path('search/',views.search, name="search"),

]