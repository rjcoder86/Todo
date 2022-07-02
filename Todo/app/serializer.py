from rest_framework.serializers import ModelSerializer

from .models import Tasks


class TaskSerilizer(ModelSerializer):
    class Meta():
        model=Tasks
        fields='__all__'