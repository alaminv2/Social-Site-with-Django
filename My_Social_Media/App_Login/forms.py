from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_Profile_Model


class Sign_Up_Form(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder':'Email'}), required=True)
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder' : 'Username'}), required=True)

    password1 = forms.CharField(
        required = True, label="",
        widget = forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required = True, label="",
        widget = forms.PasswordInput(attrs={'placeholder':'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class Edit_Profile_Form(forms.ModelForm):
    dob = forms.DateField(label="", widget=forms.TextInput(attrs={
        'type' : 'date',
        'placeholder' : 'Date Of Birth'
    }))
    contact = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder' : 'Mobile No'}))
    website = forms.URLField(required=False, label="", widget=forms.TextInput(attrs={'placeholder' : 'Web Refference'}))
    fb_acc = forms.URLField(required=False, label="", widget=forms.TextInput(attrs={'placeholder' : 'Facebook Account'}))
    pro_pic = forms.ImageField(label="")
    full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder' : 'Full Name'}))
    class Meta:
        model = User_Profile_Model
        exclude = ('user'),
