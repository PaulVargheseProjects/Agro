from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from officer.models import Crops, Pesticide, Irrigation, Fertilizer, Seminar
import datetime
from .models import SeminarBooking, Land, Product, Cart, ProductBooking, LandBooking, LabAppointment, UserQuery, LabType, Test
from .forms import LandForm, ProductForm, LabAppointmentForm, UserQueryForm
from accounts.models import Lab
from lab.models import LabResult
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'GET':
        return render(request, 'user/index.html')
    elif request.method == 'POST':
        product_id = request.POST.get('product_id')
        qty = request.POST.get('qty')
        product = Product.objects.get(product_id=product_id)
        Cart.objects.create(product=product, quantity=qty, user=request.user, amount=product.price*int(qty))
        return redirect('user_cart_table')

@login_required(login_url='/login/')
def no_of_items_in_cart(request):
    return JsonResponse({'no_of_items': Cart.objects.filter(user=request.user).count()})

@login_required(login_url='/login/')
def get_product_by_category(request):
    category = request.GET.get('category')
    if category == 'All':
        products = Product.objects.exclude(user=request.user)
    else:
        products = Product.objects.filter(category=category).exclude(user=request.user)
    products = list(products.values())
    return JsonResponse({'products': products}, safe=False)

@login_required(login_url='/login/')
def cart_table(request):
    carts = Cart.objects.filter(user=request.user)
    return render(request, 'user/cart_table.html', {'carts': carts})

@login_required(login_url='/login/')
def remove_cart_item(request, id):
    Cart.objects.get(cart_id=id).delete()
    return redirect('user_cart_table')

@login_required(login_url='/login/')
def check_out(request):
    if request.method == 'GET':
        grand_total = request.GET.get('gt')
        return render(request, 'user/payment.html', {'grand_total': grand_total})
    elif request.method == 'POST':
        items = Cart.objects.filter(user=request.user)
        for item in items:
            product = Product.objects.get(product_id=item.product.product_id)
            if product.stock > item.quantity:
                product.stock = product.stock - item.quantity
                product.save()
                ProductBooking.objects.create(product=item.product, quantity=item.quantity, user=request.user, amount=item.amount)
                Cart.objects.filter(user=request.user).delete()
                messages.success(request, 'Your order has been placed successfully')
                return redirect('user_index')
            else:
                messages.error(request, 'Product out of stock or quantity is greater than available stock')
                return redirect('user_cart_table')

@login_required(login_url='/login/')
def your_bookings(request):
    context = {}
    context['orders'] = ProductBooking.objects.filter(user=request.user)
    return render(request, 'user/your_orders.html', context)

@login_required(login_url='/login/')
def crops(request):
    context = {}
    context['crops'] = Crops.objects.all()
    return render(request, 'user/crops.html', context)

@login_required(login_url='/login/')
def pesticides(request):
    context = {}
    context['pesticides'] = Pesticide.objects.all()
    return render(request, 'user/pesticides.html', context)

@login_required(login_url='/login/')
def fertilizers(request):
    context = {}
    context['fertilizers'] = Fertilizer.objects.all()
    return render(request, 'user/fertilizers.html', context)

@login_required(login_url='/login/')
def irrigations(request):
    context = {}
    context['irrigations'] = Irrigation.objects.all()
    return render(request, 'user/irrigations.html', context)


#orders
@login_required(login_url='/login/')
def incoming_orders(request):
    context = {}
    context['orders'] = ProductBooking.objects.filter(product__user=request.user, status__in=[0,1,2])
    return render(request, 'user/incoming_orders.html', context)

@login_required(login_url='/login/')
def status_confirm(request, id):
    booking = ProductBooking.objects.get(pro_book_id=id)
    booking.status = 1
    booking.save()
    messages.success(request, 'Order has been confirmed')
    return redirect('user_incoming_orders')

@login_required(login_url='/login/')
def status_cancel(request, id):
    booking = ProductBooking.objects.get(pro_book_id=id)
    booking.status = 2
    booking.save()
    messages.success(request, 'Order has been cancelled')
    return redirect('user_incoming_orders')

@login_required(login_url='/login/')
def status_delivered(request, id):
    booking = ProductBooking.objects.get(pro_book_id=id)
    booking.status = 3
    booking.save()
    messages.success(request, 'Order has been delivered')
    return redirect('user_incoming_orders')

@login_required(login_url='/login/')
def order_history(request):
    context = {}
    context['orders'] = ProductBooking.objects.filter(product__user=request.user, status__in=[3])
    return render(request, 'user/order_history.html', context)

#Upcoming Seminar
@login_required(login_url='/login/')
def upcoming_seminar(request):
    if request.method == 'GET':
        context = {}
        context['seminars'] = Seminar.objects.filter(date__gte=datetime.date.today()).exclude(sem_id__in=SeminarBooking.objects.filter(user=request.user).values('seminar'))
        return render(request, 'user/seminar.html', context)
    elif request.method == 'POST':
        seminar_id = request.POST.get('seminar_id')
        seminar = Seminar.objects.get(sem_id=seminar_id)
        SeminarBooking.objects.create(seminar=seminar, user=request.user)
        return redirect('user_upcoming_seminar')

@login_required(login_url='/login/')
def seminar_booking(request):
    context = {}
    context['seminars'] = SeminarBooking.objects.filter(user=request.user)
    return render(request, 'user/seminar_bookings.html', context)

@login_required(login_url='/login/')
def delete_seminar_booking(request, id):
    SeminarBooking.objects.get(sem_book_id=id).delete()
    return redirect('user_seminar_booking')

#Create Land
@login_required(login_url='/login/')
def create_land(request):
    if request.method == 'POST':
        form = LandForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('user_manage_land')
    else:
        form = LandForm()
    return render(request, 'user/create_land.html', {'form': form})

#Manage Land
@login_required(login_url='/login/')
def manage_land(request):
    lands = Land.objects.filter(user=request.user)
    return render(request, 'user/manage_land.html', {'lands': lands})

#Edit Land
@login_required(login_url='/login/')
def edit_land(request, land_id):
    land = Land.objects.get(land_id=land_id)
    if request.method == 'POST':
        form = LandForm(request.POST, request.FILES, instance=land)
        if form.is_valid():
            form.save()
            return redirect('user_manage_land')
    else:
        form = LandForm(instance=land)
    return render(request, 'user/edit_land.html', {'form': form})

# Delete Land
@login_required(login_url='/login/')
def delete_land(request, land_id):
    land = Land.objects.get(land_id=land_id)
    land.delete()
    return redirect('user_manage_land')

#view Land
@login_required(login_url='/login/')
def view_land(request):
    if request.method == 'GET':
        lands = Land.objects.exclude(user=request.user).exclude(land_id__in=LandBooking.objects.filter(status=1).values('land_id'))
        return render(request, 'user/view_land.html', {'lands': lands})
    elif request.method == 'POST':
        land_id = request.POST.get('land_id')
        land = Land.objects.get(land_id=land_id)
        try:
            obj = LandBooking.objects.get(land=land, user=request.user)
            messages.error(request, 'You have already booked this land')
            return redirect('user_view_land')
        except:
            LandBooking.objects.create(land=land, user=request.user)
            messages.success(request, 'Land has been booked')
            return redirect('user_view_land')

@login_required(login_url='/login/')
def land_booking(request):
    context = {}
    context['lands'] = LandBooking.objects.filter(land__user=request.user, status=0)
    return render(request, 'user/land_request.html', context)

@login_required(login_url='/login/')
def accept_land_booking(request, id):
    booking = LandBooking.objects.get(land_book_id=id)
    booking.status = 1
    booking.save()
    messages.success(request, 'Land has been accepted')
    return redirect('user_land_booking')

@login_required(login_url='/login/')
def reject_land_booking(request, id):
    booking = LandBooking.objects.get(land_book_id=id)
    booking.status = 2
    booking.save()
    messages.success(request, 'Land has been rejected')
    return redirect('user_land_booking')

@login_required(login_url='/login/')
def land_request_status(request):
    context = {}
    context['lands'] = LandBooking.objects.filter(user=request.user)
    return render(request, 'user/land_request_status.html', context)

#Products
@login_required(login_url='/login/')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('user_manage_product')
    else:
        form = ProductForm()
    return render(request, 'user/create_product.html', {'form': form})

@login_required(login_url='/login/')
def manage_product(request):
    if request.method == 'GET':
        products = Product.objects.filter(user=request.user)
        return render(request, 'user/manage_product.html', {'products': products})
    elif request.method == 'POST':
        category = request.POST.get('product_category')
        if category == 'all':
            products = Product.objects.filter(user=request.user)
        else:
            products = Product.objects.filter(category=category,user=request.user)
        return render(request, 'user/manage_product.html', {'products': products, 'category': category})

@login_required(login_url='/login/')
def edit_product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('user_manage_product')
    else:
        form = ProductForm(instance=product)
    return render(request, 'user/edit_product.html', {'form': form})

@login_required(login_url='/login/')
def delete_product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect('user_manage_product')


# Lab
@login_required(login_url='/login/')
def lab_appointment(request):
    if request.method == 'GET':
        context = {}
        context['labs'] = LabType.objects.all()
        context['form'] = LabAppointmentForm()
        return render(request, 'user/appointment.html', context)
    elif request.method == 'POST':
        form = LabAppointmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            test = Test.objects.get(test_id=request.POST.get('test'))
            obj.test = test
            obj.user = request.user
            obj.save()
            messages.success(request, 'Appointment has been booked')
            return redirect('user_lab_appointment')
        return render(request, 'user/appointment.html', {'form': form})

@login_required(login_url='/login/')
def lab_appointment_status(request):
    context = {}
    context['appointments'] = LabAppointment.objects.filter(user=request.user)
    return render(request, 'user/appointment_status.html', context)

@login_required(login_url='/login/')
def get_all_tests(request):
    lab_id = request.GET.get('lab_id')
    tests = Test.objects.filter(lab_type=lab_id)
    return JsonResponse({'tests':list(tests.values())}, safe=False)

@login_required(login_url='/login/')
def result_details(request, id):
    result = LabResult.objects.get(lab_appointment=id)
    return render(request, 'user/result_details.html', {'result': result})

@login_required(login_url='/login/')
def user_query_list(request):
    if request.method == 'GET':
        queries = UserQuery.objects.filter(user=request.user)
        return render(request, 'user/user_query.html', {'queries': queries})

@login_required(login_url='/login/')
def create_query(request):
    if request.method == 'GET':
        return render(request, 'user/create_query.html', {'form': UserQueryForm()})
    elif request.method == 'POST':
        form = UserQueryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Query has been sent')
            return redirect('user_user_query')
        return render(request, 'user/create_query.html', {'form': form})

@login_required(login_url='/login/')
def delete_query(request, query_id):
    query = UserQuery.objects.get(query_id=query_id)
    query.delete()
    return redirect('user_user_query')

@login_required(login_url='/login/')
def query_details(request, query_id):
    query = UserQuery.objects.get(query_id=query_id)
    return render(request, 'user/query_details.html', {'q': query})
