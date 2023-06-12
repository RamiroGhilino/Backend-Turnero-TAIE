from rest_framework import viewsets
from .serializer import *
from turnero.models import *

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class RoleView(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class CareerView(viewsets.ModelViewSet):
    serializer_class = CareerSerializer
    queryset = Career.objects.all()

class AreaView(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()

class AcademicUnitView(viewsets.ModelViewSet):
    serializer_class = AcademicUnitSerializer
    queryset = AcademicUnit.objects.all()

class AcademicYearView(viewsets.ModelViewSet):
    serializer_class = AcademicYearSerializer
    queryset = AcademicYear.objects.all()

class TutorUserReviewView(viewsets.ModelViewSet):
    serializer_class = TutorUserReviewSerializer
    queryset = TutorUserReview.objects.all()

class TutorshipInstanceView(viewsets.ModelViewSet):
    serializer_class = TutorshipInstanceSerializer
    queryset = TutorshipInstance.objects.all()

class PostulationView(viewsets.ModelViewSet):
    serializer_class = PostulationSerializer
    queryset = Postulation.objects.all()

class TutorshipReportView(viewsets.ModelViewSet):
    serializer_class = TutorshipReportSerializer
    queryset = TutorshipReport.objects.all()
    
class TutorUserScheduleView(viewsets.ModelViewSet):
    serializer_class = TutorUserScheduleSerializer
    queryset = TutorUserSchedule.objects.all()

class User_X_TutorshipInstance_X_Role_View(viewsets.ModelViewSet):
    serializer_class = User_X_TutorshipInstance_X_Role_Serializer
    queryset = User_X_Tutorship_Instance_X_Role.objects.all()

class User_X_Area_View(viewsets.ModelViewSet):
    serializer_class = User_X_Area_Serializer
    queryset = User_X_Area.objects.all()
    
class User_X_Role_View(viewsets.ModelViewSet):
    serializer_class = User_X_Role_Serializer
    queryset = User_X_Role.objects.all()

class Career_X_Area_View(viewsets.ModelViewSet):
    serializer_class = Career_X_Area_Serializer
    queryset = Career_X_Area.objects.all()
    
class Career_X_User_View(viewsets.ModelViewSet):
    serializer_class = Career_X_User_Serializer
    queryset = Career_X_User.objects.all()

class Postulation_X_Area_View(viewsets.ModelViewSet):
    serializer_class = Postulation_X_Area_Serializer
    queryset = Postulation_X_Area.objects.all()