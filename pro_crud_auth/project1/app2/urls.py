from django.urls import path
from .import views

urlpatterns=[
    path('reg/',views.RegisterUser.as_view(),name='register_url'),
    path('in/',views.LoginUser.as_view(),name='login_url'),
    path('out/',views.LogoutUser.as_view(),name='logout_url'),
    path('otp/',views.VerifyOtp.as_view(),name='verify_otp'),
    #path('resend-otp/',views.ResendOTP.as_view(),name='resend_otp')
    
]