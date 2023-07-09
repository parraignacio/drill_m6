from django.urls import path
from .views import indexView, AddVehiculoView, ListVehiculoView, registro_view, login_view, logout_view

urlpatterns = [
    path('', indexView, name='index'),
    path('add/', AddVehiculoView.as_view(), name='addVehiculo'),
    path('list/', ListVehiculoView.as_view(), name='listVehiculo'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]