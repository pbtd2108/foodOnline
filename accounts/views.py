from django.http import HttpResponse
from django.shortcuts import render

from accounts.forms import UserForm

# Create your views here.

def registeruser(request):
    form=UserForm()
    context={
        'form':form,
    }
    return render(request,'accounts/registerUser.html', context)