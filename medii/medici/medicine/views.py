from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from medicine.forms import Medicineforms
from medicine.models import Medicine
from datetime import datetime
# Create your views here.

# Signup Page
def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirm password')
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("The User Name Is Already Exits.")
        
        if password != confirmpassword:
            return HttpResponse("Your Password & Confirm Password are not same.")
        else:
            my_User=User.objects.create_user(username,email,password)
            my_User.save()
            return render("login")
                
    return render (request,'signup.html')

# Login Page
def loginpage(request):
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
# home page
@login_required(login_url='login')
def homepage(request):
    obj = Medicine.objects.all()
    current = datetime.now() .date()
    x = datetime.now().date()
    context={
        'data':obj,
        'current_date': current,
        'x':x
      
    }
    return render (request,'home.html',context)

# Create Page
@login_required(login_url='login')
def create(request):
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

# Search
@login_required(login_url='login')
def search(request):
    if 'search' in request.GET:
        search=request.GET['search']
        obj=Medicine.objects.filter(mname__icontains=search)
        context={
            'search': search,
            'data': obj
        }
    return render (request,'home.html',context)


# Delete Page
@login_required(login_url='login')
def delete(request,id):
    obj = Medicine.objects.get(pk=id)
    obj.delete()
    return render (request,'delete.html')

# Update Page
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

# Logout Page
def logoutpage(request):
    logout(request)
    return redirect('login')

