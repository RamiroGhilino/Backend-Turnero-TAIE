from django.urls import path, include
from rest_framework import routers
from .views import *
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()

router.register(r'users', UserView, 'user') # /users
router.register(r'roles', RoleView, 'role') # /roles
router.register(r'careers', CareerView, 'career') # /careers
router.register(r'areas', AreaView, 'area') # /areas
router.register(r'academic-units', AcademicUnitView, 'academic-unit') # /academic-units
router.register(r'academic-years', AcademicYearView, 'academic-year') # /academic-years
router.register(r'tutor-user-reviews', TutorUserReviewView, 'tutor-user-review') # /tutor-user-reviews
router.register(r'tutorship-instances', TutorshipInstanceView, 'tutorship-instance') # /tutorship-instances
router.register(r'postulations', PostulationView, 'postulation') # /postulations
router.register(r'tutorship-reports', TutorshipReportView, 'tutorship-report') # /tutorship-reports
router.register(r'tutor-user-schedules', TutorUserScheduleView, 'tutor-user-schedule') # /tutor-user-schedules
router.register(r'user-x-tutorship-instance-x-role', User_X_TutorshipInstance_X_Role_View, 'user-x-tutorship-instance-x-role') # /user-x-tutorship-instance-x-role
router.register(r'user-x-area', User_X_Area_View, 'user-x-area') # /user-x-area
router.register(r'user-x-role', User_X_Role_View, 'user-x-role') # /user-x-role
router.register(r'career-x-area', Career_X_Area_View, 'career-x-area') # /career-x-area
router.register(r'career-x-user', Career_X_User_View, 'career-x-user') # /career-x-user
router.register(r'postulation-x-area', Postulation_X_Area_View, 'postulation-x-area') # /postulation-x-area


urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # get .yaml OpenAPI doc 
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'), # render with SwaggerUI the doc for the API
    path('api/', include(router.urls)), #GET, POST, PUT, DELETE of all models
    
] 
