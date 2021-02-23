from rest_framework_recursive.fields import RecursiveField
from rest_framework import serializers
from .models import CourseCategory, School, Course 


class CourseCategorySerializer(serializers.ModelSerializer):
    """Сериализатор категорий курсов"""

    children = RecursiveField(many=True)
    class Meta:
        model = CourseCategory
        fields = ['parent_id', 'name', 'slug', 'description', 'children']


class SchoolSerializer(serializers.ModelSerializer):
    """"Сериализация школ"""
    class Meta:
        model = School
        fields = ['title', 'slug']


class SchoolDetailSerializer(serializers.ModelSerializer):
    """Детализация школы"""
    class Meta:
        model = School
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    """"Сериализация школ"""
    class Meta:
        model = School
        fields = ['title', 'url', 'slug', 'partner_link', 'picture']


class CourseSerializer(serializers.ModelSerializer):
    """Сериализация курсов"""
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
                    'school_name',
        ]

