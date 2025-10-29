from django.shortcuts import render
from .models import Routine_Order, Duty_Roster, Message  # Added Duty_Roster
from .serializers import RoutineOrderSerializer, DutyRosterSerializer, MessageSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response

class RoutineOrderViewSet(generics.ListCreateAPIView):  # Changed to ModelViewSet for full CRUD
    serializer_class = RoutineOrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Soldiers only see active orders from their unit
        if self.request.user.role == 'soldier':
            return Routine_Order.objects.filter(unit=self.request.user.unit, is_active=True)
        # RSM and Commanders see all orders from their unit (active and inactive)
        return Routine_Order.objects.filter(unit=self.request.user.unit)
    
    def perform_create(self, serializer):
        # Only allow RSM and Commanders to create orders
        if self.request.user.role in ['rsm', 'commander']:
            serializer.save(poster=self.request.user, unit=self.request.user.unit, is_active=True)
        else:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You don't have permission to create routine orders.")

class DutyRosterViewSet(generics.ListCreateAPIView):  # Added Duty Roster view
    serializer_class = DutyRosterSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Soldiers only see active rosters from their unit
        if self.request.user.role == 'soldier':
            return Duty_Roster.objects.filter(unit=self.request.user.unit, is_active=True)
        # RSM and Commanders see all rosters from their unit
        return Duty_Roster.objects.filter(unit=self.request.user.unit)
    
    def perform_create(self, serializer):
        # Only allow RSM and Commanders to create rosters
        if self.request.user.role in ['rsm', 'commander']:
            serializer.save(poster=self.request.user, unit=self.request.user.unit, is_active=True)
        else:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You don't have permission to create duty rosters.")

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Only commanders can view messages from their unit
        if self.request.user.role == 'commander':
            return Message.objects.filter(unit=self.request.user.unit)
        # Soldiers and RSM cannot view messages (only create)
        return Message.objects.none()
    
    def perform_create(self, serializer):
        # All authenticated users can create messages
        serializer.save(unit=self.request.user.unit)
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
class RegisterView(generics.CreateAPIView):
    from .serializers import RegisterSerializer
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    def perform_create(self, serializer):
        serializer.save()
        
from rest_framework import generics, permissions
from .serializers import UserSerializer

class UserProfileView(generics.RetrieveAPIView):
    """
    Get the current user's profile
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user