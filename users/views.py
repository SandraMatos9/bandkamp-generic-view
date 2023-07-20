from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
# from utils.mixin import CreateModelMixin, ListModelMixi
from rest_framework.permissions import IsAuthenticated
from users.models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class UserView(ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated,IsAccountOwner]

    queryset=User.objects.all()
    serializer_class= UserSerializer

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return User.objects.all()
    #     return User.objects.filter(user=self.request.user)


    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
   


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset=User.objects.all()
    serializer_class =UserSerializer