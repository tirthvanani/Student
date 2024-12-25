from django.shortcuts import render, redirect
from .models import Data, Contact


# Create your views here.

def home(request):
    datas = Data.objects.all()
    context = {
        'data':datas
    }
    return render(request,'home.html',context)

def details(request, pk):
    data = Data.objects.get(id=pk)
    context = {'data': data}
    return render(request, 'details.html', context)

def add(request):
    if request.method == 'POST':
        roll = request.POST.get('sroll')
        name = request.POST.get('sname')
        course = request.POST.get('scourse') 
        address = request.POST.get('saddress') 
        Data.objects.create(
            sroll=roll,
            sname=name,
            scourse=course,
            saddress=address
        )
        return redirect('home')
    return render(request, 'add.html')

def update_data(request, uk):
    ab = Data.objects.get(id=uk)
    if request.method =='POST':
        roll = request.POST.get('roll')
        name = request.POST.get('name')
        course = request.POST.get('course') 
        address = request.POST.get('address')
        ab.sroll = roll
        ab.sname = name
        ab.scourse = course
        ab.saddress = address
        ab.save()
        return redirect('home')
    context ={
        'data':ab
    }
    return render(request, 'update.html',context)

def delete_data(request, pk):
    ab = Data.objects.get(id=pk)
    if request.method =='POST':
        ab.delete()
        return redirect('home')
    context={
        'data':ab
    }
    return render(request,'delete.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        message = request.POST.get('cmessage') 

        Contact.objects.create(cname=name, cemail=email, cmessage=message)
        
        return redirect('con_msg')
    
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def con_msg(request):
    return render(request, 'con_msg.html')