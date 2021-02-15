from django.urls import path
from .views import SchoolView, CourseView, CourseCategoryView, SchoolDetailView


urlpatterns = [
    path('course/', CourseView.as_view(), name="list_courses"),
    path('school/', SchoolView.as_view(), name="list_school"),
    path('school/<slug:slug>/', SchoolDetailView.as_view(), name="detail_school"),
    path('category/', CourseCategoryView.as_view(), name="list_category"),
]
