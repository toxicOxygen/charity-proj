from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserProfileForm

# Create your views here.
class UpdateProfileView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        form = UserProfileForm(instance=self.request.user)
        return render(self.request,'account/user/profile.html',{'form':form})
    
    def post(self,*args,**kwargs):
        form = UserProfileForm(instance=self.request.user,data=self.request.POST,files=self.request.FILES)

        if form.is_valid():
            form.save()
        return render(self.request,'account/user/profile.html',{'form':UserProfileForm(instance=self.request.user)})