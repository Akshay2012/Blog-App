from django.shortcuts import render,redirect

#Django provides user creation form in form of a class
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .forms import user_register,update_user_form,update_profile_form
from django.contrib.auth.decorators import login_required



def register(request):
    
    if request.method== "POST":
        # form=UserCreationForm(request.POST) 
        form=user_register(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get("username")
            messages.success(request,f'Account Created for {username}!. You can now login.')  #THIS IS FLASH MESSSAGE!
            return redirect('login')
            
    else:
        # form=UserCreationForm()     
        form=user_register()
    return render(request,'users/register.html',{'form':form})



@login_required
def profile(request):

    if request.method=='POST':
        uform=update_user_form(request.POST,instance=request.user)
        pform=update_profile_form(request.POST,request.FILES,instance=request.user.profile)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request,f'YOUR ACCOUNT IS UPDATED')
            return redirect('profile')


    else:
        uform=update_user_form(instance=request.user)
        pform=update_profile_form(instance=request.user.profile)
    context={
        'uform':uform,
        'pform':pform
    }
    return render(request,"users/profile.html",context=context)









#------- ALL MESSAGE OPTIONS---
# message.info
# message.debug
# message.warning
# message.error
# message.success