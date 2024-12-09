from django.shortcuts import render, redirect
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion, Allergen, CartItem
from .forms import SuggestionForm, AllergenForm, CartItemForm

def home(request):
    flavors = SeasonalFlavor.objects.all()
    allergens = Allergen.objects.all()
    return render(request, 'cafe/home.html', {'flavors': flavors, 'allergens': allergens})

def add_suggestion(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SuggestionForm()
    return render(request, 'cafe/add_suggestion.html', {'form': form})

def add_allergen(request):
    if request.method == 'POST':
        form = AllergenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AllergenForm()
    return render(request, 'cafe/add_allergen.html', {'form': form})

def manage_cart(request):
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cart')
    else:
        form = CartItemForm()
    cart_items = CartItem.objects.all()
    return render(request, 'cafe/cart.html', {'form': form, 'cart_items': cart_items})

def search_flavors(request):
    query = request.GET.get('query')
    flavors = SeasonalFlavor.objects.filter(name__icontains=query)
    return render(request, 'cafe/search.html', {'flavors': flavors})
