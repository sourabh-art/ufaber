from rest_framework import serializers
from .models import Projects,Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=("__all__")
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=("__all__")