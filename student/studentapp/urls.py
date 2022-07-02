
from django.urls import path, include
from .views import student_list, update_student

urlpatterns = [
    path('list/',student_list),
    path('<int:pk>',update_student)
]
