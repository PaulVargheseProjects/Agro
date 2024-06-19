from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='officer_index'),
    #Crops
    path('create_crops/', create_crops, name='officer_create_crops'),
    path('manage_crops/', manage_crops, name='officer_manage_crops'),
    path('edit_crops/<int:pk>/', edit_crops, name='officer_edit_crops'),
    path('delete_crops/<int:pk>/', delete_crops, name='officer_delete_crops'),
    path('crop_change_status/<int:pk>', crop_status_change, name="officer_crop_status_change"),
    #Pesticide
    path('create_pesticide/', create_pesticide, name='officer_create_pesticide'),
    path('manage_pesticide/', manage_pesticide, name='officer_manage_pesticide'),
    path('edit_pesticide/<int:pk>/', edit_pesticide, name='officer_edit_pesticide'),
    path('delete_pesticide/<int:pk>/', delete_pesticide, name='officer_delete_pesticide'),
    path('pesticide_change_status/<int:pk>', pesticide_status_change, name="officer_pesticide_status_change"),
    #Fertilizer
    path('create_fertilizer/', create_fertilizer, name='officer_create_fertilizer'),
    path('manage_fertilizer/', manage_fertilizer, name='officer_manage_fertilizer'),
    path('edit_fertilizer/<int:pk>/', edit_fertilizer, name='officer_edit_fertilizer'),
    path('delete_fertilizer/<int:pk>/', delete_fertilizer, name='officer_delete_fertilizer'),
    path('fertilizer_change_status/<int:pk>', fertilizer_status_change, name="officer_fertilizer_status_change"),
    #irrigation
    path('create_irrigation/', create_irrigation, name='officer_create_irrigation'),
    path('manage_irrigation/', manage_irrigation, name='officer_manage_irrigation'),
    path('edit_irrigation/<int:pk>/', edit_irrigation, name='officer_edit_irrigation'),
    path('delete_irrigation/<int:pk>/', delete_irrigation, name='officer_delete_irrigation'),
    path('irrigation_change_status/<int:pk>', irrigation_status_change, name="officer_irrigation_status_change"),
    #lab
    # path('create_lab/', create_lab, name='officer_create_lab'),
    path('manage_lab/', manage_lab, name='officer_manage_lab'),
    # path('edit_lab/<int:pk>/', edit_lab, name='officer_edit_lab'),
    path('delete_lab/<int:pk>/', delete_lab, name='officer_delete_lab'),
    #seminar
    path('create_seminar/', create_seminar, name='officer_create_seminar'),
    path('manage_seminar/', manage_seminar, name='officer_manage_seminar'),
    path('edit_seminar/<int:pk>/', edit_seminar, name='officer_edit_seminar'),
    path('delete_seminar/<int:pk>/', delete_seminar, name='officer_delete_seminar'),
    path('accept_seminar/<int:pk>/', accept_seminar, name='officer_accept_seminar'),
    path('reject_seminar/<int:pk>/', reject_seminar, name='officer_reject_seminar'),
    #Seminar
    path('seminar_booking/', seminar_booking, name='officer_seminar_booking'),
    #Scheme
    path('create_scheme/', create_scheme, name='officer_create_scheme'),
    path('manage_scheme/', manage_scheme, name='officer_manage_scheme'),
    path('delete_scheme/<int:pk>/', delete_scheme, name='officer_delete_scheme'),
    #User Query
    path('user_query/', user_query_list, name='officer_user_query'),
    path('user_query/<int:pk>/', user_query_detail, name='officer_user_query_detail'),
    path('query_reply/<int:pk>/', query_reply, name='officer_query_reply'),
]