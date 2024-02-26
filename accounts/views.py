from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages ,auth

from accounts.forms import UserForm
from accounts.utils import detectUser,send_verification_email
from vendor.forms import VendorForm
from .models import User, UserProfile
from .utils import detectUser,send_verification_email,activate_user
from django.contrib.auth.decorators import login_required

# Create your views here.

def registeruser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('myAccount')
    # elif request.method =='POST':
    elif request.method=='POST':
        form=UserForm(request.POST)

        if form.is_valid():
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # form.save()
            # return redirect('registeruser')
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            
            # send verification email
            activate_user(request,user)
            messages.error(request, "Your account has been registered successfully!")
            print("user is created")
            return redirect('registeruser')
        else:
            print("invalid form")
            print(form.errors)
    else:
        form=UserForm()  
    context={
        'form':form,
    }
    return render(request,'accounts/registerUser.html', context)

def registerVendor(request): 
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('myAccounnt')
    elif request.method =='POST':
    # if request.method == "POST":
        #Store Data
        form=UserForm(request.POST)
        v_form=VendorForm(request.POST,request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.VENDOR
            user.save()
            vendor=v_form.save(commit=False)
            vendor.user=user
            user_profile=UserProfile.objects.get(user=user)
            vendor.user_profile=user_profile
            vendor.save()
            # send verification email
            send_verification_email(request,user)
            messages.success(request,'your restaurant has been registered successfully ! pls wait for approval')
            messages.error(request, "Your vendor has been registered successfully!")
            print("vendor is created")
            return redirect('registerVendor')
            
        else:
            print("invalid form")
            print(form.errors)        
        
    else:                    
        form=UserForm()
        v_form=VendorForm()
    context={
        'form':form,
        'v_form': v_form, 
    }
    return render(request,'accounts/registerVendor.html',context)

def activate(request, uidb64,token):
    #Activate the user by setting the is_activate status is True
    pass

def login(request):  
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('myAccount')
    elif request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user= auth.authenticate(email=email , password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'you are logged out')
    return redirect('login')

def dashboard(request):
    print("inside dashboard...............................................")
    return render(request,'accounts/dashboard.html')

@login_required(login_url='login')
def myAccount(request):
    user=request.user
    redirectUrl=detectUser(user)
    return redirect(redirectUrl)

@login_required(login_url='login')
def custDashboard(request):
    print("inside custDashboard...............................................")
    return render(request,'accounts/custDashboard.html')


@login_required(login_url='login')
def vendorDashboard(request):
    print("inside vendorDashboard...............................................")
    return render(request,'accounts/vendorDashboard.html')
