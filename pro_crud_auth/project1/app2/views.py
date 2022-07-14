from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django.views import View
from django.conf import settings
from random import randint
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.

def generate_otp():
    return randint(1000,9999)
    

class RegisterUser(View):
     template_name = 'app2/register.html'
     form  = RegistrationForm
     def get(self,request):
         form  = self.form()
         context ={'form':form}
         return render(request,self.template_name,context)
     def post(self,request):
         form = self.form(request.POST)
         if form.is_valid():
             form.save()
             name = request.POST.get('username')
             mail = request.POST.get('email')
             
             subject = "Welcome to python world"
             message = f"Hello,{name} , {mail} You are successfully register for python world."
             email_from = settings.EMAIL_HOST_USER
             email_to =[mail,]
             send_mail(subject,message,email_from,email_to) 
             form.save()
             return redirect('login_url')
         context={'form':form}
         return render(request,self.template_name,context)      
     
     
class LoginUser(View):
    template_name= 'app2/login.html'
    def get(self,request):
        context={}
        return render(request,self.template_name,context) 
    def post(self,request):
        un =request.POST.get('u')
        pw = request.POST.get('p')
        
        user =  authenticate(username=un , password = pw)
        otp = generate_otp()
        subject = "Welcome to world"
        message = f"Hello , Your one time otp {otp} for login."
        email_from = settings.EMAIL_HOST_USER
        email_to =[user.email,]
        send_mail(subject,message,email_from,email_to)
        
        response = render(request=request,template_name='app2/otp.html',context={'user':user})
        response.set_cookie('otp',otp,max_age=120)
        return response
        


            
class VerifyOtp(View):
    def post(self,request):
        otp = request.POST.get('otp')
        if otp:
            otp1 = request.COOKIES.get('otp')
            if otp == otp1:
                try:
                    user_id = request.POST.get('user')
                    user = User.objects.get(pk = user_id)
                except User.DoesNotExist:
                    print("USER NOT FOUND")
                login(request,user)
                response = redirect("show_url")
                response.delete_cookie("otp")
                return response
            user_id = request.POST.get('user')
            user = User.objects.get(pk = user_id)
            response = render(request=request,template_name='app2/otp.html',context = {'user':user})
            return response
        return HttpResponse("Invalid otp")
    
    
               

    

    


class LogoutUser(View):
    def get(self,request):
        logout(request)
        return redirect('login_url')
         
        














'''
class ResendOTP(View):
    template_name = 'app2/otp.html'
    def post(self,request):
        user = request.POST.get('user')
        user = User.objects.get(pk=user)
        request.COOKIES.pop('otp')
        otp = generate_otp()
        
        send_mail("OTP_Verification",
        f"One time OTP for login is {otp}",
        settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently = False)
        
        resp = render(request,self.template_name,context={'user':user})
        resp.set_cookie('otp',otp,max_age=30)
        return resp 
'''