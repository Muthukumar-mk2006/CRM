from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('accounts.urls')
    ),

    path(
        'leads/',
        include('leads.urls')
    ),
    path(
    'customers/',
    include('customers.urls')
),
path(
    'employees/',
    include('employees.urls')
),
path(
    'services/',
    include('services.urls')
),
path(
    'reports/',
    include('reports.urls')
),
path(
    'forgot-password/',
    auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt',
        success_url='/forgot-password/done/'
    ),
    name='password_reset'
),

path(
    'forgot-password/done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ),
    name='password_reset_done'
),

path(
    'reset-password/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url='/reset-password/complete/'
    ),
    name='password_reset_confirm'
),

path(
    'reset-password/complete/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ),
    name='password_reset_complete'
),
    

]