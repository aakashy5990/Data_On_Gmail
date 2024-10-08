# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)


# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 
        'placeholder': 'Your Message'
    }))
