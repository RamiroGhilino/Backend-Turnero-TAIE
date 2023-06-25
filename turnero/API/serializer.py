from rest_framework import serializers
from turnero.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
    
class AcademicUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicUnit
        fields = '__all__'
    
class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = '__all__'
        
class TutorUserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorUserReview
        fields = '__all__'
    
class TutorshipInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorshipInstance
        fields = '__all__'
    
class PostulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation
        fields = '__all__'
    
class TutorshipReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorshipReport
        fields = '__all__'
        
class TutorUserScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TutorUserSchedule
        fields = '__all__'

class User_X_TutorshipInstance_X_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_X_Tutorship_Instance_X_Role
        fields = '__all__'
        
class User_X_Area_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_X_Area
        fields = '__all__'
        
class User_X_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_X_Role
        fields = '__all__'
        
class Career_X_Area_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Career_X_Area
        fields = '__all__'
        
class Career_X_User_Serializer(serializers.ModelSerializer):        
    class Meta:
        model = Career_X_User
        fields = '__all__'

class Postulation_X_Area_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Postulation_X_Area
        fields = '__all__'
