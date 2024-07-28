from django.shortcuts import render, redirect
from django.db.models import Q
from collections import defaultdict
from datetime import datetime
from .models import Booking, Room, Timetable, Course, Userdetails

def home(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        user = Userdetails.objects.get(user=request.user.id)
        room_numbers = request.POST.getlist('room')
        rooms = Room.objects.filter(
            Q(block__in=[room.split("-")[0] for room in room_numbers]) &
            Q(number__in=[room.split("-")[1] for room in room_numbers])
        )

        booking = Booking(
            reason=request.POST.get('reason'),
            user=user,
            starttime=request.POST.get('start_time'),
            endtime=request.POST.get('end_time'),
            date=request.POST.get('date'),
            reason_text=request.POST.get('reason_text')
        )
        booking.save()
        booking.rooms.add(*rooms)
        return redirect('home')

    current_date = request.GET.get('datetime', datetime.today().strftime('%Y-%m-%d'))
    current_time = request.GET.get('time', '17:00')
    current_time2 = request.GET.get('time2', '19:00')

    bookings = Booking.objects.filter(
        Q(isWaiting=True) |
        (Q(isWaiting=False) & Q(isApproved=True)),
        starttime__lt=current_time2, endtime__gt=current_time,
        cancel=False, date=current_date
    )
    booked_room_ids = bookings.values_list('rooms', flat=True)

    timetable = Timetable.objects.filter(
        day_of_week=datetime.strptime(current_date, '%Y-%m-%d').strftime('%A')[:3].upper(),
        stime__lt=current_time2, etime__gt=current_time
    )
    timetable_room_ids = timetable.values_list('room', flat=True)

    pending_bookings = Booking.objects.filter(
        starttime__lt=current_time2, endtime__gt=current_time, cancel=False,
        date=current_date, isApproved=False
    )
    pending_room_ids = pending_bookings.values_list('rooms', flat=True)

    room_status = defaultdict(list)
    room_status_count = defaultdict(int)

    for room in Room.objects.all():
        if room.id in booked_room_ids or room.id in timetable_room_ids or \
           room.available_st.strftime('%H:%M') > current_time or room.available_et.strftime('%H:%M') < current_time2:
            status = 0
        elif room.id in pending_room_ids:
            status = 2
        else:
            status = 1
            room_status_count[room.block] += 1

        course_code = None
        if room.id in timetable_room_ids:
            course_id = timetable.get(room=room.id).course.id
            course_code = Course.objects.get(id=course_id).tcode

        room_status[room.block].append((room, status, course_code))

    context = {
        'title': "Home",
        'room_status': dict(room_status),
        'room_status_count': dict(room_status_count),
        'reason_choices': REASON_CHOICES,
        'current_date': current_date,
        'current_time': current_time,
        'current_time2': current_time2,
    }

    return render(request, 'home.html', context)
