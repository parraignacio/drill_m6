from django.contrib import admin
from django.urls import include, path

from vehiculo.views import indexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name='index'),
    path('vehiculo/', include(('vehiculo.urls', 'vehiculo'), namespace='vehiculo')),
]

