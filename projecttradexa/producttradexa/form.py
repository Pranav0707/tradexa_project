from .models import *
from django.forms import ModelForm


class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'