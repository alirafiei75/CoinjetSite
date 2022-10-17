from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'

class PasswordResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']