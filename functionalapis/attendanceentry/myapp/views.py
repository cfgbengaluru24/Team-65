from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, DailyReport

def index(request):
    students = Student.objects.all()
    if request.method == 'POST':
        topic_taught = request.POST.get('topic_taught')
        DailyReport.objects.create(topic_taught=topic_taught)
        return redirect('index')
    return render(request, 'index.html', {'students': students})

def toggle_attendance(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.is_present = not student.is_present
    student.save()
    return redirect('index')
