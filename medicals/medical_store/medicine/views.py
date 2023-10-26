from django.shortcuts import render,redirect,HttpResponse
from medicine.models import Medicine
from medicine.forms import Medicineforms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
#home page
@login_required(login_url='login')
def homepage(request):
    obj = Medicine.objects.all()
    context={
        'data':obj,
    }
    return render(request,'home.html',context)
#create
@login_required(login_url='login')
def addpage(request):
     if request.method == "POST":
        form = Medicineforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
     else:
        form = Medicineforms
     context={
        'form': form
    }
     
     return render (request,'create.html',context)
#update
@login_required(login_url='login')
def update(request,id):
    obj = Medicine.objects.get(pk=id)
    if request.method == "POST":
        form = Medicineforms(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Medicineforms(instance=obj)
    context={
        'form': form
    }
    return render (request,'update.html',context)

#delete
@login_required(login_url='login')
def delete(request,id):
    obj = Medicine.objects.get(pk=id)
    obj.delete()
    return render (request,'delete.html')

#search
def search(request):
    if 'search' in request.GET:
        search=request.GET['search']
        obj=Medicine.objects.filter(name__icontains=search)
        context={
            'search': search,
            'data': obj
        }
    return render (request,'home.html',context)

# Signup Page
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("The User Name Is Already Exits.")
        
        if password != confirmpassword:
            return HttpResponse("Your Password & Confirm Password are not same.")
        else:
            my_User=User.objects.create_user(username,email,password)
            my_User.save()
            return redirect("login")
                
    return render (request,'signup.html')

# Login Page
def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("User Name or Password is Incorrect.")
    return render (request,'login.html')
#logout
def Logout(request):
    logout(request)
    return redirect('login')


