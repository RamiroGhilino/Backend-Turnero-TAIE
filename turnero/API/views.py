from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import *
from turnero.models import *
from drf_spectacular.utils import extend_schema, inline_serializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    @extend_schema(
        summary="Look up for a user by email",
        description="""This endpoint is a POST method, but it does not create any new user.
        It only looks up for a user by email. Reason for this decision was to not expose emails in the URL.""",
        request=inline_serializer(
            name= "EmailLookUpSerializer",
            fields={
                "email": serializers.EmailField()
            },
        ),
        responses={
            200: UserSerializer,
            400: inline_serializer(
                name= "400-serializer",
                fields={
                    "message": serializers.CharField()
                }
            ),
            404: inline_serializer(
                name= "404-serializer",
                fields={
                    "message": serializers.CharField()
                    }
                )
        },
    )
    @action(detail=False, methods=['POST'], url_path='is-user')
    def is_user(self, request):
        if not request.data['email'].endswith('@ucc.edu.ar'):
            content = {'message': 'Invalid email'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        try: 
            user = User.objects.get(email=request.data['email'])
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            content = {'message': 'Not matching user with email'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

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