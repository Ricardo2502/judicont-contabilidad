from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Judicont Contabilidad</title>
            </head>
            <body style="font-family:sans-serif; text-align:center; margin-top:100px;">
                <h1>🎯 Bienvenido a Judicont Contabilidad</h1>
                <p>Tu sistema contable está funcionando correctamente.</p>
                <p>Muy pronto aquí verás el catálogo de cuentas, diario contable y reportes financieros.</p>
            </body>
        </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),  # Esta es la vista básica de inicio
]
