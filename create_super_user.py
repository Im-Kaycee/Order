import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order.settings')
django.setup()

from django.contrib.auth import get_user_model
from main.models import Unit  

User = get_user_model()

# Create or get a unit
unit, created = Unit.objects.get_or_create(name="Headquarters", description="Admin Unit")

# Create superuser
user = User.objects.create_superuser(
    username="militaryadmin",
    password="admin123",
    email="admin@military.com",
    role="commander",
    trade="administration",
    rank="general",
    unit=unit
)

print(f"Superuser created: {user.username}")