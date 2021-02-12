from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Course, CourseCategory, School
from .serializers import SchoolSerializer, CourseSerializer
from _datetime import date


class SchoolView(ListAPIView):
    """Список школ"""
    model = School
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class CourseView(ListAPIView):
    """Список курсов"""
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(date_start__gte=date.today())