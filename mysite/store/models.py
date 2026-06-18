from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    slug = models.SlugField(max_length=100, unique=True, blank=True) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField(blank=True) 
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0.00) 
    image = models.ImageField(upload_to='products/', blank=True, null=True) 
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) 

    def __str__(self):
        return self.name



