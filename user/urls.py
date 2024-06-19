from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='user_index'),
    path('get_product_by_category/', get_product_by_category, name='user_get_product_by_category'),
    path('cart_table/', cart_table, name='user_cart_table'),
    path('remove_cart_item/<int:id>/', remove_cart_item, name='user_remove_cart_item'),
    path('no_of_items_in_cart/', no_of_items_in_cart, name='user_no_of_items_in_cart'),
    path('check_out/', check_out, name='user_check_out'),
    path('your_bookings/', your_bookings, name='user_your_bookings'),
    path('incoming_orders/', incoming_orders, name='user_incoming_orders'),
    path('status_confirm/<int:id>/', status_confirm, name='user_status_confirm'),
    path('status_cancel/<int:id>/', status_cancel, name='user_status_cancel'),
    path('status_delivered/<int:id>/', status_delivered, name='user_status_delivered'),
    path('order_history/', order_history, name='user_order_history'),
    #agriculture products
    path('crops/', crops, name='user_crops'),
    path('pesticides/', pesticides, name='user_pesticides'),
    path('fertilizers/', fertilizers, name='user_fertilizers'),
    path('irrigations/', irrigations, name='user_irrigations'),
    # seminar
    path('upcoming_seminar/', upcoming_seminar, name='user_upcoming_seminar'),
    path('seminar_booking/', seminar_booking, name='user_seminar_booking'),
    path('delete_seminar_booking/<int:id>', delete_seminar_booking, name='user_delete_seminar_booking'),
    # land
    path('create_land/', create_land, name='user_create_land'),
    path('manage_land/', manage_land, name='user_manage_land'),
    path('delete_land/<int:land_id>', delete_land, name='user_delete_land'),
    path('update_land/<int:land_id>', edit_land, name='user_update_land'),
    path('view_land/', view_land, name='user_view_land'),
    path('land_booking/', land_booking, name='user_land_booking'),
    path('accept_land_booking/<int:id>', accept_land_booking, name='user_accept_land_booking'),
    path('reject_land_booking/<int:id>', reject_land_booking, name='user_reject_land_booking'),
    path('land_request_status/', land_request_status, name='user_land_request_status'),
    # product
    path('create_product/', create_product, name='user_create_product'),
    path('manage_product/', manage_product, name='user_manage_product'),
    path('delete_product/<int:product_id>', delete_product, name='user_delete_product'),
    path('update_product/<int:product_id>', edit_product, name='user_update_product'),
    #lab
    path('lab_appointment/', lab_appointment, name='user_lab_appointment'),
    path('lab_appointment_status/', lab_appointment_status, name='user_lab_appointment_status'),
    path('lab_result/<int:id>/', result_details, name='user_lab_result'),
    path('get_all_tests/', get_all_tests, name='user_get_all_tests'),
    #UserQuery
    path('user_query/', user_query_list, name='user_user_query'),
    path('create_query/', create_query, name='user_create_query'),
    path('delete_query/<int:query_id>', delete_query, name='user_delete_query'),
    path('query_details/<int:query_id>', query_details, name='user_query_details'),
]