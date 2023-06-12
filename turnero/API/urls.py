from django.urls import path, include
from rest_framework import routers
from .views import UserView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()

router.register(r'users', UserView, 'user') # /users

urlpatterns = [
    path('api/', include(router.urls)), #GET, POST, PUT, DELETE of User
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
] 
