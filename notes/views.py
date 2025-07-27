from django.shortcuts import render
from .serializers import TaskSerializer, RegistrationSerializer
from .models import Task
from .permissions import IsAuthorOrSuperuser
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthorOrSuperuser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.action == 'list':
            if not self.request.user.is_authenticated:
                return Task.objects.none()
            if self.request.user.is_superuser:
                return Task.objects.all()
            return Task.objects.filter(user=self.request.user)
        return Task.objects.all()


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
