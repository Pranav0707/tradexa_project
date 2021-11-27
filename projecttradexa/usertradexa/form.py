from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import *

from django.forms import ModelForm
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']


class PostForm(ModelForm):
    class Meta:
        model=Post
        fields='__all__'