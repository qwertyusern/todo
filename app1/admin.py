
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


@admin.register(Student)
class StudentAdmin(ModelAdmin):
    search_fields = ("id","ism")

@admin.register(Reja)
class StudentAdmin(ModelAdmin):
    search_fields = ("id","stu")


