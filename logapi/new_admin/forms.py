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

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['ct_id'].queryset = Category.objects.all()
        self.fields['ct_id'].label_from_instance = lambda obj: obj.ct_name 

        self.fields['br_id'].queryset = Brand.objects.all()
        self.fields['br_id'].label_from_instance = lambda obj: obj.br_name 
    class Meta:
        model=Products
        fields="__all__"
        widgets={
            "pr_id":forms.NumberInput(attrs={"class":"form-control","placeholder":"Product Id"}),
            "pr_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Product Name"}),
            "ct_id":forms.Select(attrs={"class":"form-control","placeholder":"Category"}),
            "br_id":forms.Select(attrs={"class":"form-control","placeholder":"Brand"}),
            "stock":forms.NumberInput(attrs={"class":"form-control","placeholder":"Stock"}),
            "price":forms.TextInput(attrs={"class":"form-control","placeholder":"Price"}),
            "images":forms.FileInput(),
            "status":forms.Select(attrs={"class":"form-control","placeholder":"Product status"}),
            }
        
class BannerForm(forms.ModelForm):
    class Meta:
        model=Banner
        fields="__all__"
        widgets={
            "bn_id":forms.NumberInput(),
            "photo":forms.FileInput()
        }