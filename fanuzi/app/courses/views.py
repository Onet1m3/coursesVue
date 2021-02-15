from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Course, CourseCategory, School
from .serializers import SchoolSerializer, CourseSerializer, CourseCategorySerializer
from _datetime import date


class SchoolView(ListAPIView):
    """Список школ"""
    model = School
    permission_classes = [AllowAny,]
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class CourseView(ListAPIView):
    """Список курсов"""
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(date_start__gte=date.today())


class CourseCategoryView(ListAPIView):
    model = CourseCategory
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects.filter(parent_id__isnull=True)