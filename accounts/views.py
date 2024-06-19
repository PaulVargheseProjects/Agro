from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CommonForm, LabForm, LabExtraForm, CForm
from django.contrib import messages
from officer.models import Scheme

# Create your views here.

def index(request):
    context = {}
    context['schemes'] = Scheme.objects.all()[::-1]
    return render(request, 'accounts/index.html', context)

#login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user.user_type == 'officer':
                return redirect('/officer/')
            elif user.user_type == 'lab':
                return redirect('/lab/')
            elif user.user_type == 'user':
                return redirect('user_index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

#logout
def logout_view(request):
    logout(request)
    return redirect('accounts_login')

#user signup
def user_signup(request):
    if request.method == 'POST':
        form = CommonForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.set_password(form.cleaned_data.get('password'))
            obj.user_type = 'user'
            obj.save()
            messages.success(request, 'Account successfully created!')
            return redirect('accounts_login')
    else:
        form = CommonForm()
    return render(request, 'accounts/user_signup.html', {'form': form})

def common_reg(request):
    if request.method == 'GET':
        form = CForm()
        context = {'form': form}
        return render(request, 'accounts/common.html', context)
    elif request.method == 'POST':
        form = CForm(request.POST)
        if form.is_valid():
            obj1 = form.save(commit=False)
            obj1.set_password(form.cleaned_data['password'])
            obj1.user_type = request.POST['user_type']
            obj1.aadhar = 'None'
            obj1.address = 'None'
            obj1.save()
            messages.success(request, 'Account successfully created!')
            return redirect('accounts_login')
        else:
            context = {'form': form}
            return render(request, 'accounts/common.html', context)



