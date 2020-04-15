from django.shortcuts import render
from django.views.generic import TemplateView,View
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['acc_home'] = "active"
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['acc_about'] = 'active'
        return context


class ContactPageView(View):
    def get(self,*args,**kwargs):
        form = ContactForm()
        return render(self.request,'pages/contacts.html',{'form':form,"acc_contact":"active"})
    
    def post(self,*args,**kwargs):
        form = ContactForm(data=self.request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = "An email from {}".format(cd['email'])
            send_mail(subject,cd['message'],cd['email'],['kwakukusi30@yahoo.com'])

        return render(self.request,'pages/contacts.html',{'form':ContactForm(),"acc_contact":"active"})

class GalleryView(TemplateView):
    template_name = 'pages/gallery.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['acc_gallery'] = 'active'
        return context