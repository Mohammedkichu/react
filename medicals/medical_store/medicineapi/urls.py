from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logout, name='login_api'),
    path('medicinelist', views.medicinelist, name='medicines_api'),
    path('add', views.add, name='create_api'),
    path('update/<int:pk>', views.update, name='update_api'),
    path('search/<str:name>', views.search, name='search_api'),
    path('delete/<int:id>', views.delete, name='delete_api'),
    path('signup',views.signup,name='register'),
    path('login',views.login,name='loginapi'),
]