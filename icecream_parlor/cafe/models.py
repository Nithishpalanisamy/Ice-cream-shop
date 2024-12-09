from django.db import models

class SeasonalFlavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    available_from = models.DateField()
    available_to = models.DateField()

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class CustomerSuggestion(models.Model):
    flavor = models.CharField(max_length=100)
    allergy_concerns = models.TextField()

    def __str__(self):
        return self.flavor

class Allergen(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    flavor = models.ForeignKey(SeasonalFlavor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.flavor.name}"
