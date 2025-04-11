
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_contable.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

print("🚀 Ejecutando migraciones...")
call_command('migrate')

# Crear superusuario si no existe
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✅ Superusuario creado: admin / admin123")
else:
    print("ℹ El superusuario 'admin' ya existe.")
