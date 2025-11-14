from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),            
    path('inventario/', include('inventario.urls')), 
    path('personal/', include('personal.urls')),     
    path('mesas/', include('mesas.urls')),           
    path('facturacion/', include('facturacion.urls')), 

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)