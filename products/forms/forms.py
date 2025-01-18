from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['createdAt']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter title"}),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter price"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "image": forms.TextInput(attrs={"class": "form-control"}),
            "inStock": forms.CheckboxInput(attrs={"class": "form-check-input"})
        }