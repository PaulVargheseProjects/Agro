from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='lab_index'),
    path('appointments/', appointments, name='lab_appointments'),
    path('confirm_appointment/<int:id>/', confirm_appointment, name='lab_confirm_appointment'),
    path('cancel_appointment/<int:id>/', cancel_appointment, name='lab_cancel_appointment'),
    path('appointment_list/', appointment_list, name='lab_appointment_list'),
    path('result/<int:id>/', lab_result, name='lab_result'),
    path('result_details/<int:id>/', result_details, name='lab_result_details'),
    path('user_query/', user_query_list, name='lab_user_query'),
    path('user_query/<int:pk>/', user_query_detail, name='lab_user_query_detail'),
    path('query_reply/<int:pk>/', query_reply, name='lab_query_reply'),
]