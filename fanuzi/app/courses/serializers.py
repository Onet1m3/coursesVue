from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers
from .models import CourseCategory, School, Course 


class CourseCategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий курсов"""

    children = RecursiveField(many=True)
    class Meta:
        model = CourseCategory
        fields = '__all__'

   


class SchoolSerializer(serializers.ModelSerializer):
    """"Сериализация школ"""
    class Meta:
        model = School
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    """Сериализация курсов"""
    category = CourseCategorySerializer()
    school_name = SchoolSerializer()

    class Meta:
        model = Course
        fields = [
                    'title', 
                    'description', 
                    'slug', 
                    'date_start', 
                    'date_end', 
                    'amount', 
                    'installment', 
                    'raiting', 
                    'category', 
                    'school_name',
        ]

