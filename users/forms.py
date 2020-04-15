from django import forms
from django.contrib.auth import get_user_model

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','email','photo','instagram_url','twitter_url','facebook_url']