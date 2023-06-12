from rest_framework import viewsets
from .serializer import UserSerializer
from turnero.models import User

# Create your views here.
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()