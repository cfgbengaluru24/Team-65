from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
path('login/', views.loginprofile, name='login'),
    # path('profile/', views.userprofile, name='userprofile'),
    # path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('student/', views.student, name='student'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('volunteerregistration/', views.volunteerregistration, name='volunteerregistration'),
    path('circleLeader/', views.circleLeader, name='circleLeader'),
    path('mapping/', views.circleLeader, name='match_students_to_volunteers'),
    path('volunteerlearning', views.volunteerlearning,name="volunteerlearning"),
path('chat/', views.chat, name='chat'),

    # path('change-password/<str:uidb64>/<str:token>/', views.change_password, name='change-password'),
    # path('email/', views.send_email_api, name='send_email_api'),
    # path('new_email/', views.new_email, name='new_email'),

    # path('room-option/<str:pk>', views.roomoption, name='roomoption'),
    # path('adminuserprofile/<str:pk>', views.adminuserprofile, name='adminuserprofile'),

    # path('analytics/', views.analytics, name='analytics'),
    # path('timetable/<str:pk>', views.timetable, name='timetable'),
    # path('allsociety/', views.allsociety, name='allsociety'),

]
