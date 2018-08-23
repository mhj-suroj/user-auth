from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter First Name' }))
    last_name = forms.CharField(label="", max_length=100,  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Last Name'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    username = forms.CharField(label="", help_text='<small><ul class="form-text text-muted"><li>Must be combination of letters and digits.</li></ul></small>',
                               max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    password1 = forms.CharField(label="", max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
                                help_text='<small><ul class="form-text text-muted"><li>Must contain at least 8 characters.</li><li>Must be combination of letters, digits and special-characters.</li></ul></small>')
    password2 = forms.CharField(label="", max_length=100, help_text='<small><ul class="form-text text-muted"><li>Enter the same password as above.</li></ul></small>',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', ) # OR ('__all__', )

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password', )
