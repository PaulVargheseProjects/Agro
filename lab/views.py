from django.shortcuts import redirect, render
from user.models import LabAppointment, LabType, Test
from accounts.models import User, Lab
from .models import LabResult
from .forms import LabResultForm
from django.contrib.auth.decorators import login_required
from officer.forms import UserQuery, QueryReplyForm
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    # return render(request, 'lab/home.html')
    return redirect('lab_appointments')

@login_required(login_url='/login/')
def appointments(request):
    labs = LabType.objects.all()
    if request.method == 'GET':
        appointments = LabAppointment.objects.filter(status=0)
        context = {}
        context['appointments'] = appointments
        context['labs'] = labs
        return render(request, 'lab/appointments.html', context)
    elif request.method == 'POST':
        appointments = LabAppointment.objects.filter(status=0, test__test_id=request.POST['test'])
        context = {}
        context['appointments'] = appointments
        context['labs'] = labs
        return render(request, 'lab/appointments.html', context) 

@login_required(login_url='/login/')
def confirm_appointment(request, id):
    appointment = LabAppointment.objects.get(lab_book_id=id)
    appointment.status = 1
    appointment.save()
    messages.success(request, 'Appointment confirmed')
    return redirect('lab_appointments')

@login_required(login_url='/login/')
def cancel_appointment(request, id):
    appointment = LabAppointment.objects.get(lab_book_id=id)
    appointment.status = 2
    appointment.save()
    messages.success(request, 'Appointment cancelled')
    return redirect('lab_appointments')

@login_required(login_url='/login/')
def appointment_list(request):
    appointments = LabAppointment.objects.filter(status__in=[1,3])
    return render(request, 'lab/appointment_list.html', {'appointments': appointments})

@login_required(login_url='/login/')
def lab_result(request, id):
    appointment = LabAppointment.objects.get(lab_book_id=id)
    if request.method == 'POST':
        form = LabResultForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.lab_appointment = appointment
            obj.save()
            appointment.status = 3
            appointment.save()
            messages.success(request, 'Lab result added')
            return redirect('lab_appointment_list')
    else:
        form = LabResultForm()
    return render(request, 'lab/result.html', {'form': form})

@login_required(login_url='/login/')
def result_details(request, id):
    result = LabResult.objects.get(lab_appointment=id)
    return render(request, 'lab/result_details.html', {'result': result})


@login_required(login_url='/login/')
def user_query_list(request):
    if request.method == 'GET':
        queries = UserQuery.objects.filter(to=2)
        return render(request, 'lab/user_query.html', {'queries': queries})

@login_required(login_url='/login/')
def user_query_detail(request, pk):
    query = UserQuery.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'lab/user_query_detail.html', {'q': query})
    elif request.method == 'POST':
        reply = request.POST.get('reply')
        if query.reply != reply:
            query.reply = reply
            query.save()
            messages.success(request, 'Reply successfully sent!')
        else:
            messages.warning(request, 'Reply already sent!')
        return redirect('lab_user_query_detail', pk=pk)

@login_required(login_url='/login/')
def query_reply(request, pk):
    query = UserQuery.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'lab/query_reply.html', {'form': QueryReplyForm(instance=query)})
    elif request.method == 'POST':
        query.reply = request.POST['reply']
        query.save()
        messages.success(request, 'Reply successfully sent!')
        return redirect('lab_user_query')