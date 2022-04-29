from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlar/', student),
    path('rejalar/', reja),
    path('reja_edit/<int:p>/',reja_edit),
    path('student_edit/<int:p>/',reja_edit),
]
