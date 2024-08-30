from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import PasswordResetForm

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address', 'mobile', 'profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'description', 'product_image','reorderlevel','qunatity']

class ADDProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'description', 'product_image']


class ProductFormup(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name',  'description', 'product_image','reorderlevel','qunatity']

# Address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile = forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['name', 'feedback']

# For updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Orders
        fields = ['status']

# For contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# Custom password reset form
class CustomPasswordResetForm(PasswordResetForm):
    pass
