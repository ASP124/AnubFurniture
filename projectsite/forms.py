from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":9, "cols":25,"style":"resize:none;"}))
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone_number', 'subject', 'message']

class SubscribeForm(forms.Form):
    email = forms.EmailField()
        
