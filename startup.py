
import os
import django
from django.core.management import call_command
from django.contrib.auth import get_user_model

print("🚀 Iniciando proceso de migraciones y superusuario...")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_contable.settings")
django.setup()

print("🔄 Ejecutando migraciones...")
call_command("migrate")

print("👤 Verificando superusuario...")
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "admin123")
    print("✅ Superusuario creado: admin / admin123")
else:
    print("ℹ El superusuario ya existe")

print("🚀 Iniciando servidor...")
os.system("gunicorn sistema_contable.wsgi")
