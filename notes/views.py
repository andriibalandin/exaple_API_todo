from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from .permissions import IsAuthorOrSuperuser
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthorOrSuperuser]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Task.objects.none()
        if self.request.user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user)
    