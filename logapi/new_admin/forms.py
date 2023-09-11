from django import forms
from api.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
        widgets={
            "ct_id":forms.NumberInput(attrs={"class":"form-control","placeholder":"catgory id"}),
            "ct_name":forms.TextInput(attrs={"class":"form-control","placeholder":"category name"}),
            "status":forms.TextInput(attrs={"class":"form-control"})
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "br_id":forms.NumberInput(attrs={"class":"form-control","placeholder":"Brand Id"}),
            "br_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Brand Name"}),
            "status":forms.TextInput(attrs={"class":"form-control"})
        }
