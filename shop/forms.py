
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'image']#,'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'description':
                field.widget.attrs.update({
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Enter product description',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': f'Enter {field_name}',
                })
