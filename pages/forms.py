from django import forms
# from phone_field import PhoneFormField

class ContactForm(forms.Form):
    email = forms.EmailField()
    # phone = PhoneFormField(help_text='Phone')
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=50)

