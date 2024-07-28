from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .models import Student, Volunteer, Subject, Preference, Feedback
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q, Count
from datetime import datetime, time, date
from collections import defaultdict
import csv, os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render

from datetime import date, timedelta
from django.utils import timezone


def loginprofile(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')

        if username == 'user1@gmail.com':
            return redirect('student')
        if username == 'user2@gmail.com':
            return redirect('volunteer')
        if username == 'user2@gmail.com':
            return redirect('circleLeader')
        # if True:
        #     password = request.POST.get('password')
        #     print(username, password)
        #     try:
        #         user = User.objects.get(username=username)
        #     except:
        #         messages.error(request, 'error')
        #
        #     user = authenticate(request, username=username, password=password)
        #     if user is not None:
        #         login(request, user)
        #         return redirect('student')
        #     else:
        #         messages.error(request, 'error')

    context = {'title': "Login"}
    return render(request, 'login.html', context)


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # existing_user = Student.objects.get(email=email, First_name=First_name, Last_name=Last_name)

        if True:
            if password == password2:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                # user_details.save()

                # send_email('signup', [email])
                return redirect('login')
            else:
                messages.error(request, 'error')
        else:
            redirect('student')
            messages.error(request, 'error')

    context = {
        'title': 'Sign Up',
    }
    return render(request, 'signup.html', context)


def generate_weekly_preferences():
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())  # Monday of the current week

    students = Student.objects.all()
    volunteers = Volunteer.objects.all()
    subjects = Subject.objects.all()

    for day_offset in range(7):
        current_day = start_of_week + timedelta(days=day_offset)
        for student in students:
            preferred_subjects = student.preferred_subjects.all()
            for subject in preferred_subjects:
                for volunteer in volunteers.filter(subjects=subject):
                    Preference.objects.get_or_create(
                        student=student,
                        volunteer=volunteer,
                        subject=subject,
                        week_start_date=start_of_week,
                        day_of_week=day_offset
                    )


def circleLeader(request):
    preferences = Preference.objects.filter(
        week_start_date=timezone.now().date() - timedelta(days=timezone.now().date().weekday()))[:10]
    student_feedback = Feedback.objects.filter(by="student")[:10]
    volunteer_feedback = Feedback.objects.filter(by="volunteer")[:10]
    context = {'preferences': preferences, 'student_feedback': student_feedback,
               'volunteer_feedback': volunteer_feedback, 'arr': [0] * 5, 'val1': 0, 'val2': 0, 'val3': 0,
               'title': 'Circle Leader'}
    if request.method == "POST":
        context = {'preferences': preferences, 'student_feedback': student_feedback,
                   'volunteer_feedback': volunteer_feedback, 'arr': [0] * 5, 'val1': 120, 'val2': 325, 'val3': 125,'title': 'Circle Leader'}
        return render(request, 'circleLeader.html', context)
        # generate_weekly_preferences()
    return render(request, 'circleLeader.html', context)


def student(request):
    if request.method == 'POST':
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        attendance = request.POST.get('attendance', 0)
        Feedback.objects.create(by="student", preference=request.POST['preference_id'],
                                question1=q1, question2=q2, question3=q3, question4=q4, question5=q5,
                                volunteer_attended=attendance)
        return render(request, 'matching/feedback_success.html')

    student = Student.objects.get(email='charlie.davis@example.com')
    today = timezone.now().date()
    start_of_current_week = today - timedelta(days=today.weekday())  # Monday of current week
    start_of_previous_week = start_of_current_week - timedelta(days=7)  # Monday of previous week

    current_week_preferences = Preference.objects.filter(
        student=student,
        week_start_date=start_of_current_week
    ).order_by('day_of_week')

    previous_week_preferences = Preference.objects.filter(
        student=student,
        week_start_date=start_of_previous_week
    ).order_by('day_of_week')

    context = {
        'current_week_preferences': current_week_preferences,
        'previous_week_preferences': previous_week_preferences,
        'student': student,
        'title': 'Student'
    }

    return render(request, 'student.html', context)


def volunteer(request):
    if request.method == 'POST':
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        attendance = request.POST['attendance']
        Feedback.objects.create(by="volunteer", preference=Preference.objects.get(id=request.POST['preference_id']),
                                question1=q1, question2=q2, question3=q3, question4=q4, question5=q5,
                                volunteer_attended=attendance)
        return render(request, 'volunteer.html')

    if request.method == "POST" and "submit" in request.POST:
        val = request.POST.getlist('rsvp')
        for i in val:
            Preference.objects.get
        vol = Preference.objects.filter(volunteer=volunteer, week_start_date=start_of_current_week)

    volunteer = Volunteer.objects.get(user=4)

    today = timezone.now().date()
    start_of_current_week = today - timedelta(days=today.weekday())  # Monday of current week
    start_of_previous_week = start_of_current_week - timedelta(days=7)  # Monday of previous week

    current_week_preferences = Preference.objects.filter(
        volunteer=volunteer,
        week_start_date=start_of_current_week
    ).order_by('day_of_week')

    previous_week_preferences = Preference.objects.filter(
        volunteer=volunteer,
        week_start_date=start_of_previous_week
    ).order_by('day_of_week')

    context = {
        'current_week_preferences': current_week_preferences,
        'previous_week_preferences': previous_week_preferences,
        'volunteer': volunteer,
    'title': 'Volunteer'
    }

    return render(request, 'volunteer.html', context)


def volunteerregistration(request):
    context={'title': 'Volunteer Registration'}
    return render(request, "volunteerregistration.html")


def chat(request):
    context = {'title': 'Chat'}
    return render(request, "chat.html")


def volunteerlearning(request):
    context = {'title': 'Volunteer Learning'}
    return render(request, "volunteerlearning.html")
