from django.shortcuts import render,redirect
from .models import *
from .form import *
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):
    return render(request,'home.html')

def departments(request):
    dict={
        'dep':Departments.objects.all()
    }
    return render(request,'department.html',dict)

def booking(request):
    if request.method == 'GET':
        context={}
        context['form']=BookingForm()
        return render(request,'booking.html',context)
    elif request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
         context={}
         context['form']=BookingForm()
         return render(request,'booking.html',context)
  

def doctors(request):
    doct={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctor.html',doct)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')



class DocDetailView(DetailView):
   model = Doctors
   template_name = 'docdetail.html'
   context_object_name = 'doc'
   