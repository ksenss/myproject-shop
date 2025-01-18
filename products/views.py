from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime
from products.forms.forms import ProductForm
from products.models import Product


# Create your views here.
def index(request):
     products = Product.objects.all()
     return render(request, "index.html", { "products": products })

def create(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create.html", { "form": form })
    
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "create.html", { "form": form })
def delete(request, id):
       product = get_object_or_404(Product, id=id)
       product.delete()
       return redirect("/")
def details(request, id):
    product = get_object_or_404(Product, id=id)
    
    return render(request, "details.html", { "item": product })
def edit(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, "edit.html", { "form": form })
    
    form = ProductForm(request.POST, instance=product)

    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "edit.html", { "form": form })