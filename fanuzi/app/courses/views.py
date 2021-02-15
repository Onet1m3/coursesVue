from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Course, CourseCategory, School
from .serializers import SchoolSerializer, CourseSerializer, CourseCategorySerializer, SchoolDetailSerializer
from _datetime import date


class SchoolView(ListAPIView):
    """Список школ"""
    model = School
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class SchoolDetailView(APIView):
    """Детализация школы"""
    
    def get_object(self, slug):
        return School.objects.get(slug=slug)

    def get(self, request, slug):
        school = self.get_object(slug)
        serializer = SchoolDetailSerializer(school)
        return Response(serializer.data)


class CourseView(ListAPIView):
    """Список курсов"""
    model = Course
    serializer_class = CourseSerializer
    queryset = Course.objects.filter(date_start__gte=date.today())


class CourseCategoryView(ListAPIView):
    model = CourseCategory
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects.filter(parent_id__isnull=True, active=True)