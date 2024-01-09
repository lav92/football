from django import forms
from shop.models import Order


class OrderForm(forms.ModelForm):
    delivery = forms.CheckboxInput()

    class Meta:
        model = Order
        fields = ['phone', 'address', 'delivery', 'delivery_date']
        labels = {
            'delivery': 'Доставка',
        }
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter your Address'}),
            'phone': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Enter phone number'}),
        }
