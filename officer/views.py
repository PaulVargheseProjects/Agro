from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import CropsForm, PesticideForm, FertilizerForm, SeminarForm, IrrigationForm, SchemeForm, QueryReplyForm
from .models import Crops, Pesticide, Fertilizer, Irrigation, Seminar, Scheme
from accounts.models import Lab, User
from user.models import SeminarBooking, UserQuery
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    context = {}
    context['schemes'] = Scheme.objects.all()[::-1]
    return render(request, 'officer/home.html', context)

@login_required(login_url='/login/')
def create_crops(request):
    if request.method == 'GET':
        form = CropsForm()
        context = {'form': form, 'title': 'Create Crops'}
        return render(request, 'officer/create.html', context)
    elif request.method == 'POST':
        form = CropsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Crops successfully created!')
            return redirect('officer_create_crops')
        else:
            context = {'form': form, 'title': 'Create Crops'}
            return render(request, 'officer/create.html', context)

@login_required(login_url='/login/')
def manage_crops(request):
    crops = Crops.objects.all()
    context = {'datas': crops, 'title': 'Manage Crops'}
    return render(request, 'officer/manage_crops.html', context)

@login_required(login_url='/login/')
def edit_crops(request, pk):
    crops = Crops.objects.get(pk=pk)
    if request.method == 'GET':
        form = CropsForm(instance=crops)
        context = {'form': form, 'title': 'Edit Crops'}
        return render(request, 'officer/edit.html', context)
    elif request.method == 'POST':
        form = CropsForm(request.POST, request.FILES, instance=crops)
        if form.is_valid():
            form.save()
            messages.success(request, 'Crops successfully updated!')
            return redirect('officer_manage_crops')
        else:
            context = {'form': form, 'title': 'Edit Crops'}
            return render(request, 'officer/edit.html', context)

@login_required(login_url='/login/')
def delete_crops(request, pk):
    crops = Crops.objects.get(pk=pk)
    crops.delete()
    messages.success(request, 'Crops successfully deleted!')
    return redirect('officer_manage_crops')

@login_required(login_url='/login/')
def crop_status_change(request, pk):
    crop = Crops.objects.get(pk=pk)
    if crop.is_available:
        crop.is_available = False
    else:
        crop.is_available = True
    crop.save()
    return redirect('officer_manage_crops')

@login_required(login_url='/login/')
def irrigation_status_change(request, pk):
    irri = Irrigation.objects.get(pk=pk)
    if irri.is_available:
        irri.is_available = False
    else:
        irri.is_available = True
    irri.save()
    return redirect('officer_manage_irrigation')

@login_required(login_url='/login/')
def pesticide_status_change(request, pk):
    pest = Pesticide.objects.get(pk=pk)
    if pest.is_available:
        pest.is_available = False
    else:
        pest.is_available = True
    pest.save()
    return redirect('officer_manage_pesticide')

@login_required(login_url='/login/')
def fertilizer_status_change(request, pk):
    fert = Fertilizer.objects.get(pk=pk)
    if fert.is_available:
        fert.is_available = False
    else:
        fert.is_available = True
    fert.save()
    return redirect('officer_manage_fertilizer')



@login_required(login_url='/login/')
def create_pesticide(request):
    if request.method == 'GET':
        form = PesticideForm()
        context = {'form': form, 'title': 'Create Pesticide'}
        return render(request, 'officer/create.html', context)
    elif request.method == 'POST':
        form = PesticideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pesticide successfully created!')
            return redirect('officer_create_pesticide')
        else:
            context = {'form': form, 'title': 'Create Pesticide'}
            return render(request, 'officer/create.html', context)

@login_required(login_url='/login/')
def manage_pesticide(request):
    pesticides = Pesticide.objects.all()
    context = {'datas': pesticides, 'title': 'Manage Pesticide'}
    return render(request, 'officer/manage_pesti.html', context)

@login_required(login_url='/login/')
def edit_pesticide(request, pk):
    pesticide = Pesticide.objects.get(pk=pk)
    if request.method == 'GET':
        form = PesticideForm(instance=pesticide)
        context = {'form': form, 'title': 'Edit Pesticide'}
        return render(request, 'officer/edit.html', context)
    elif request.method == 'POST':
        form = PesticideForm(request.POST, request.FILES, instance=pesticide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pesticide successfully updated!')
            return redirect('officer_manage_pesticide')
        else:
            context = {'form': form, 'title': 'Edit Pesticide'}
            return render(request, 'officer/edit.html', context)

@login_required(login_url='/login/')
def delete_pesticide(request, pk):
    pesticide = Pesticide.objects.get(pk=pk)
    pesticide.delete()
    messages.success(request, 'Pesticide successfully deleted!')
    return redirect('officer_manage_pesticide')

@login_required(login_url='/login/')
def create_fertilizer(request):
    if request.method == 'GET':
        form = FertilizerForm()
        context = {'form': form, 'title': 'Create Fertilizer'}
        return render(request, 'officer/create.html', context)
    elif request.method == 'POST':
        form = FertilizerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fertilizer successfully created!')
            return redirect('officer_create_fertilizer')
        else:
            context = {'form': form, 'title': 'Create Fertilizer'}
            return render(request, 'officer/create.html', context)

@login_required(login_url='/login/')
def manage_fertilizer(request):
    fertilizers = Fertilizer.objects.all()
    context = {'datas': fertilizers, 'title': 'Manage Fertilizer'}
    return render(request, 'officer/manage_ferti.html', context)

@login_required(login_url='/login/')
def edit_fertilizer(request, pk):
    fertilizer = Fertilizer.objects.get(pk=pk)
    if request.method == 'GET':
        form = FertilizerForm(instance=fertilizer)
        context = {'form': form, 'title': 'Edit Fertilizer'}
        return render(request, 'officer/edit.html', context)
    elif request.method == 'POST':
        form = FertilizerForm(request.POST, request.FILES, instance=fertilizer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fertilizer successfully updated!')
            return redirect('officer_manage_fertilizer')
        else:
            context = {'form': form, 'title': 'Edit Fertilizer'}
            return render(request, 'officer/edit.html', context)

@login_required(login_url='/login/')
def delete_fertilizer(request, pk):
    fertilizer = Fertilizer.objects.get(pk=pk)
    fertilizer.delete()
    messages.success(request, 'Fertilizer successfully deleted!')
    return redirect('officer_manage_fertilizer')

@login_required(login_url='/login/')
def create_irrigation(request):
    if request.method == 'GET':
        form = IrrigationForm()
        context = {'form': form, 'title': 'Create Irrigation'}
        return render(request, 'officer/create.html', context)
    elif request.method == 'POST':
        form = IrrigationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Irrigation successfully created!')
            return redirect('officer_create_irrigation')
        else:
            context = {'form': form, 'title': 'Create Irrigation'}
            return render(request, 'officer/create.html', context)

@login_required(login_url='/login/')
def manage_irrigation(request):
    irrigations = Irrigation.objects.all()
    context = {'datas': irrigations, 'title': 'Manage Irrigation'}
    return render(request, 'officer/manage_irrig.html', context)

@login_required(login_url='/login/')
def edit_irrigation(request, pk):
    irrigation = Irrigation.objects.get(pk=pk)
    if request.method == 'GET':
        form = IrrigationForm(instance=irrigation)
        context = {'form': form, 'title': 'Edit Irrigation'}
        return render(request, 'officer/edit.html', context)
    elif request.method == 'POST':
        form = IrrigationForm(request.POST, request.FILES, instance=irrigation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Irrigation successfully updated!')
            return redirect('officer_manage_irrigation')
        else:
            context = {'form': form, 'title': 'Edit Irrigation'}
            return render(request, 'officer/edit.html', context)

@login_required(login_url='/login/')
def delete_irrigation(request, pk):
    irrigation = Irrigation.objects.get(pk=pk)
    irrigation.delete()
    messages.success(request, 'Irrigation successfully deleted!')
    return redirect('officer_manage_irrigation')

@login_required(login_url='/login/')
def create_seminar(request):
    if request.method == 'GET':
        form = SeminarForm()
        context = {'form': form, 'title': 'Create Seminar'}
        return render(request, 'officer/create_seminar.html', context)
    elif request.method == 'POST':
        form = SeminarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seminar successfully created!')
            return redirect('officer_create_seminar')
        else:
            context = {'form': form, 'title': 'Create Seminar'}
            return render(request, 'officer/create_seminar.html', context)

@login_required(login_url='/login/')
def manage_seminar(request):
    seminars = Seminar.objects.all()
    context = {'seminars': seminars}
    return render(request, 'officer/manage_seminar.html', context)

@login_required(login_url='/login/')
def edit_seminar(request, pk):
    seminar = Seminar.objects.get(pk=pk)
    if request.method == 'GET':
        form = SeminarForm(instance=seminar)
        context = {'form': form, 'title': 'Edit Seminar'}
        return render(request, 'officer/edit.html', context)
    elif request.method == 'POST':
        form = SeminarForm(request.POST, request.FILES, instance=seminar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seminar successfully updated!')
            return redirect('officer_manage_seminar')
        else:
            context = {'form': form, 'title': 'Edit Seminar'}
            return render(request, 'officer/edit.html', context)

@login_required(login_url='/login/')
def delete_seminar(request, pk):
    seminar = Seminar.objects.get(pk=pk)
    seminar.delete()
    messages.success(request, 'Seminar successfully deleted!')
    return redirect('officer_manage_seminar')

@login_required(login_url='/login/')
def seminar_booking(request):
    context = {}
    context['seminars'] = SeminarBooking.objects.all()
    return render(request, 'officer/seminar_bookings.html', context)

@login_required(login_url='/login/')
def accept_seminar(request, pk):
    seminar = SeminarBooking.objects.get(pk=pk)
    seminar.status = 1
    seminar.save()
    messages.success(request, 'Seminar successfully accepted!')
    return redirect('officer_seminar_booking')

@login_required(login_url='/login/')
def reject_seminar(request, pk):
    seminar = SeminarBooking.objects.get(pk=pk)
    seminar.status = 2
    seminar.save()
    messages.success(request, 'Seminar successfully rejected!')
    return redirect('officer_seminar_booking')

@login_required(login_url='/login/')
def manage_lab(request):
    labs = User.objects.filter(user_type='lab')
    context = {'labs': labs}
    return render(request, 'officer/manage_lab.html', context)

@login_required(login_url='/login/')
def delete_lab(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.success(request, 'Lab successfully deleted!')
    return redirect('officer_manage_lab')

@login_required(login_url='/login/')
def create_scheme(request):
    if request.method == 'GET':
        form = SchemeForm()
        context = {'form': form}
        return render(request, 'officer/create_scheme.html', context)
    elif request.method == 'POST':
        form = SchemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Scheme successfully created!')
            return redirect('officer_create_scheme')
        else:
            context = {'form': form}
            return render(request, 'officer/create_scheme.html', context)

@login_required(login_url='/login/')
def manage_scheme(request):
    schemes = Scheme.objects.all()
    context = {'schemes': schemes}
    return render(request, 'officer/manage_scheme.html', context)

@login_required(login_url='/login/')
def delete_scheme(request, pk):
    scheme = Scheme.objects.get(pk=pk)
    scheme.delete()
    messages.success(request, 'Scheme successfully deleted!')
    return redirect('officer_manage_scheme')

@login_required(login_url='/login/')
def user_query_list(request):
    if request.method == 'GET':
        queries = UserQuery.objects.filter(to=1)
        return render(request, 'officer/user_query.html', {'queries': queries})

@login_required(login_url='/login/')
def user_query_detail(request, pk):
    query = UserQuery.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'officer/user_query_detail.html', {'q': query})
    elif request.method == 'POST':
        reply = request.POST.get('reply')
        if query.reply != reply:
            query.reply = reply
            query.save()
            messages.success(request, 'Reply successfully sent!')
        else:
            messages.warning(request, 'Reply already sent!')
        return redirect('officer_user_query_detail', pk=pk)

@login_required(login_url='/login/')
def query_reply(request, pk):
    query = UserQuery.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request, 'officer/query_reply.html', {'form': QueryReplyForm(instance=query)})
    elif request.method == 'POST':
        query.reply = request.POST['reply']
        query.save()
        messages.success(request, 'Reply successfully sent!')
        return redirect('officer_user_query')
