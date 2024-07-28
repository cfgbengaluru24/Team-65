from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('toggle_attendance/<int:student_id>/', views.toggle_attendance, name='toggle_attendance'),
]
