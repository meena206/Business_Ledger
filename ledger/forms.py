from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Transaction

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Email address"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Username"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"
    }), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password"
    }), label="Confirm Password")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone", "email", "city", "address"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Customer name",
                "required": True
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone number (e.g., 555-1234)",
                "required": True
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email address"
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "City"
            }),
            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Street address"
            }),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("transaction_type", "amount", "description", "date")
        widgets = {
            "transaction_type": forms.Select(attrs={
                "class": "form-select",
                "required": True
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
                "min": "0.01",
                "placeholder": "0.00",
                "required": True
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Transaction details (optional)"
            }),
            "date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
                "required": True
            }),
        }