from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),            
    path('inventario/', include('inventario.urls')), 
    path('personal/', include('personal.urls')),     
    path('mesas/', include('mesas.urls')),           
    path('facturacion/', include('facturacion.urls')), 

]
