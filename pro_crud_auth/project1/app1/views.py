from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class AddLaptop(LoginRequiredMixin,View):
    template_name = 'app1/addlaptop.html'
    form  = LaptopForm
    
    def get(self,request):
        form = self.form()
        context={'form':form}
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = self.form(request.POST)
        if form.is_valid():
            form .save()
            return redirect('show_url')
        context={'form':form}
        return render(request,self.template_name,context)
    
class ShowLaptop(LoginRequiredMixin,View):
    template_name = 'app1/showlaptop.html'
    def get(self,request):
        obj = Laptop.objects.all()
        context={'obj':obj}
        return render(request,self.template_name,context)
    
    
class UpdateLaptop(LoginRequiredMixin,View):
    template_name = 'app1/addlaptop.html'
    form  = LaptopForm
    def get(self,request,id):
        obj = Laptop.objects.get(id=id)
        form = self.form(instance=obj)
        context={'form':form}
        return render(request,self.template_name,context)
    def post(self,request,id):
        obj = Laptop.objects.get(id=id)
        form = self.form(request.POST,instance=obj)
        if form.is_valid():
            form .save()
            return redirect('show_url')
        context={'form':form}
        return render(request,self.template_name,context)
    
class DeleteLaptop(LoginRequiredMixin,View):
    template_name = 'app1/deletelaptop.html'
    def get(self,request,id):
        obj = Laptop.objects.get(id=id)
        context = {'obj':obj}
        return render(request,self.template_name,context)
    
    def post(self,request,id):
         obj = Laptop.objects.get(id=id)
         obj.delete()
         return redirect('show_url')
         context = {'obj':obj}
         return render(request,self.template_name,context)
       