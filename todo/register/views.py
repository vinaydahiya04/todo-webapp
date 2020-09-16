from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm
from .forms import UserExtraForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(data = request.POST)
        form_1 = UserExtraForm(data=request.POST)
        if form.is_valid() and form_1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form_1.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            return HttpResponseRedirect(reverse('home'))
        else:
             print("invalid form")
    else:
        form = RegisterUserForm()
        form_1 = UserExtraForm()
    return render(request,'register/register.html',{"form":form,"form1":form_1})
 
