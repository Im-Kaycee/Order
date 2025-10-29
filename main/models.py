from django.db import models
from django.contrib.auth.models import AbstractUser

class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    ROLECHOICES = (
        ('rsm', 'RSM'),
        ('soldier', 'Soldier'),
        ('commander', 'Commander'),
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    role = models.CharField(max_length=20, choices=ROLECHOICES, default='soldier')
    trade = models.CharField(max_length=100, default='general')
    rank = models.CharField(max_length=50, default='recruit')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='members')
    
    def __str__(self):
        return f"{self.rank} {self.username} - {self.unit.name}"
class Routine_Order(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_orders')
    routine_order = models.FileField(upload_to='orders/')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='routine_orders')
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.unit.name}"

class Duty_Roster(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_rosters')
    duty_roster = models.FileField(upload_to='rosters/')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='duty_rosters')
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.unit.name}"

class Message(models.Model):
    content = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='messages')
    is_anonymous = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.unit.name} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"