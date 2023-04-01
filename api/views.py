from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import ProjectSerializer

class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    def post(self, request,):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
