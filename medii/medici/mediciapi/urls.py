from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login_api'),
    path('signup', views.signup, name='signup_api'),
    path('logout', views.logout, name='login_api'),
    path('medicinelist', views.medicinelist, name='medicines_api'),
    path('add', views.add, name='create_api'),
    path('update/<int:pk>', views.update, name='update_api'),
    path('search/<str:mname>', views.search, name='search_api'),
    path('delete/<int:id>', views.delete, name='delete_api'),
]