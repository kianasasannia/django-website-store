from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product,Category

def product_list (request):
    products = Product.objects.all()
    categories=Category.objects.all()
    return render(request,'store/product_list.html',{'products':products,"categories":categories})

def product_detail(request,id):
    product=get_object_or_404(Product,id=id)
    return render(request,'product_detail.html',{'product':product})


def products_by_category (request ,category_id):
    categories=Category.objects.all()
    selected_category=get_object_or_404(Category,id=category_id)
    products=Product.objects.filter(category=selected_category)
    return render (request,"store/product_list.html",{"products":products,"categories":categories,"selected_category":selected_category})
