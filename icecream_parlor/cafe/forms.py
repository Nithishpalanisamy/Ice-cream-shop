from django import forms
from .models import CustomerSuggestion, Allergen, CartItem

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = CustomerSuggestion
        fields = ['flavor', 'allergy_concerns']

class AllergenForm(forms.ModelForm):
    class Meta:
        model = Allergen
        fields = ['name']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['flavor', 'quantity']
