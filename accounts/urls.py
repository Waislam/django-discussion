from django.urls import path

from .views import signup
from django.contrib.auth.views import (LogoutView,
										LoginView,
										PasswordResetView, 
										PasswordResetDoneView,
										PasswordResetConfirmView,
										PasswordResetCompleteView)

# app_name='accounts'

urlpatterns=[
	path('signup/', signup, name='singup' ),
	path('logout/', LogoutView.as_view(), name='logout' ),
	path('accounts/login/', LoginView.as_view( template_name ='accounts/login.html'), name='login' ),


	path('reset/', PasswordResetView.as_view( template_name ='accounts/password_reset.html',
		email_template_name='accounts/password_reset_email.html',
		subject_template_name='accounts/password_reset_subject.txt'), name='password_reset' ),
	path('reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),


	path('reset/<uidb64>/<token>/',
    	PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
    	name='password_reset_confirm'),
	
	path('reset/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
    	name='password_reset_complete'),


]