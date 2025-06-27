from rest_framework.serializers import ModelSerializer, StringRelatedField
from .models import Task


class TaskSerializer(ModelSerializer):
    user = StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['title', 'id', 'description', 'slug', 'user', 'created', 'completed']
        read_only_fieds = ['slug', 'id', 'user', 'created']
