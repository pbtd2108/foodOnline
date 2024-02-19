from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.forms import UserForm
from .models import User

# Create your views here.

def registeruser(request):
    if request.method=='POST':
        print(request.POST,"#############################################3")
        form=UserForm(request.POST)

        if form.is_valid():
            # password=form.cleaned_data['password']
            # print("2222222222222")
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # form.save()
            # print("33333333333333")
            # return redirect('registeruser')
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
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