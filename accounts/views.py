from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.forms import UserForm

# Create your views here.

def registeruser(request):
    if request.method=='POST':
        print(request.POST,"#############################################3")
        form=UserForm(request.POST)
        print("1111111111111")
        if form.is_valid():
            print("2222222222222")
            form.save()
            print("33333333333333")
            return redirect('registeruser')
    else:
        form=UserForm()  
    context={
        'form':form,
    }
    return render(request,'accounts/registerUser.html', context)