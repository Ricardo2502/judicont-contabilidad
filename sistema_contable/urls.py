from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contabilidad.urls')),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Sistema contable funcionando correctamente 🚀")
