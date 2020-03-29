from rest_framework import generics
# from django.views.decorators.csrf import csrf_exempt
# from braces.views import CsrfExemptMixin

from .models import Project, Student
from .serializers import ProjectSerializer, StudentSerializer

# @csrf_exempt


# class ListProject(CsrfExemptMixin, generics.ListCreateAPIView):
class ListProject(generics.ListCreateAPIView):
    # authentication_classes = []
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# @csrf_exempt


# class DetailProject(CsrfExemptMixin, generics.RetrieveUpdateDestroyAPIView):
class DetailProject(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = []
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ListStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
