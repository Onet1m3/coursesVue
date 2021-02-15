from django.urls import path
from .views import SchoolView, CourseView, CourseCategoryView


urlpatterns = [
    path('course/', CourseView.as_view(), name="list_courses"),
    path('school/', SchoolView.as_view(), name="list_school"),
    path('categori/', CourseCategoryView.as_view(), name="list_categori"),
]
