from rest_framework import serializers
from .models import Unit, User, Routine_Order, Duty_Roster, Message
from rest_framework_simplejwt.tokens import RefreshToken
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'role', 'trade', 'rank', 'unit', 'unit_name')
        read_only_fields = ('id', 'unit_name')
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name','last_name', 'password', 'role', 'trade', 'rank', 'unit', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_tokens(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'soldier'),
            trade=validated_data.get('trade', 'general'),
            rank=validated_data.get('rank', 'recruit'),
            unit=validated_data['unit']
        )
        return user
        
class RoutineOrderSerializer(serializers.ModelSerializer):
    poster_name = serializers.CharField(source='poster.username', read_only=True)
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    routine_order = serializers.FileField(required=True)
    
    class Meta:
        model = Routine_Order
        fields = ('id', 'poster', 'poster_name', 'routine_order', 'unit', 
                 'unit_name', 'title', 'is_active', 'created_at')
        read_only_fields = ('poster', 'created_at', 'is_active')

class DutyRosterSerializer(serializers.ModelSerializer):
    poster_name = serializers.CharField(source='poster.username', read_only=True)
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    duty_roster = serializers.FileField(required=True)
    
    class Meta:
        model = Duty_Roster
        fields = ('id', 'poster', 'poster_name', 'duty_roster', 'unit', 
                 'unit_name', 'title', 'start_date', 'end_date', 
                 'is_active', 'created_at')
        read_only_fields = ('poster', 'created_at')

    def validate(self, data):
        """
        Check that start_date is before end_date.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError({
                "end_date": "End date must be after start date"
            })
        return data

class MessageSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='unit.name', read_only=True)
    
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('timestamp',)