
import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_contable.settings")
django.setup()

User = get_user_model()

username = "admin"
password = "admin123"
email = "admin@example.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print("✔ Superusuario creado: admin / admin123")
else:
    print("ℹ El usuario 'admin' ya existe.")
