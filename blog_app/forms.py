from django import forms
from django.contrib.auth.models import User
from blog_app.models import *


class User_registrion(forms.ModelForm):
    class Meta():
        model = User
        fields=("username", "password", "email")

class post_form(forms.ModelForm):
    class Meta():
        model=posts
        fields=('headding','upload_File','description','is_it_an_Image')

class comment_form(forms.ModelForm):
    class Meta():
        model=comment
        fields=('name','text',)

        widgets={
            'name': forms.TextInput(attrs={
                'placeholder':'Your Name',
                'style':'text-align:center;font-size:1em',
                'class':'bold m-2',
            }),
            'text': forms.TextInput(attrs={
                'placeholder':'Comment',
                'style':'text-align:center',
                'class':'bold m-2',
            })
        }