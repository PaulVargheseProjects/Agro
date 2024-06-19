from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='accounts_index'),
    path('login/', login_view, name='accounts_login'),
    path('logout/', logout_view, name='accounts_logout'),
    path('user_signup/', user_signup, name='accounts_user_signup'),
    path('admininstration/accounts/signup/', common_reg, name='accounts_admin_accounts'),
]