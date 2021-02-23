from django.contrib import admin
from .models import CourseCategory, School, Course


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


# @admin.register(CoursePartner)
# class CoursePartnerAdmin(admin.ModelAdmin):
#     pass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
