from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import users_signup_view, users_account_delete_view

urlpatterns = [
    path(
        'sign-up/',
        users_signup_view,
        name='users_sign_up_view'
    ),
    path(
        'sign-in/',
        LoginView.as_view(template_name='users/users_login.html'),
        name='users_login_view'
    ),
    path(
        'sign-out/',
        LogoutView.as_view(template_name='users/users_logout.html'),
        name='users_logout_view'
    ),
    path(
        'destroy/',
        users_account_delete_view,
        name='users_account_delete_view'
    )
]
