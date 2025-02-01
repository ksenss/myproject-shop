from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, redirect, render
from products.forms.forms import ProductForm
from products.models import Product
from .models import Cart,Product
from django.contrib.sessions.models import Session
from django.contrib import messages



# Create your views here.
def index(request):
    session_id = request.session.session_key
    cart_item_count = Cart.objects.filter(session_id=session_id).count()
    query = request.GET.get('search', '')  # Отримуємо запит пошуку з URL
    if query:
        products = Product.objects.filter(title__icontains=query)  # Пошук за частиною назви товару
    else:
        products = Product.objects.all()  # Якщо пошук не введений, виводимо всі товари

    return render(request, "index.html", { "products": products, "search_query": query ,"cart_item_count": cart_item_count})


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
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)  # Отримуємо товар за його id

    # Отримуємо session_id користувача або використовуємо 'guest' для анонімних користувачів
    session_id = request.session.session_key or 'guest'  # Якщо немає сесії, можна використовувати 'guest'

    # Перевірка, чи існує вже кошик для цієї сесії
    cart_item, created = Cart.objects.get_or_create(
        session_id=session_id, 
        product=product
    )

    if created:
        cart_item.quantity = 1  # Спочатку ставимо кількість 1
        cart_item.save()
        messages.success(request, f'{product.title} added to cart!')
    else:
        cart_item.quantity += 1  # Якщо товар вже є в кошику, збільшуємо кількість
        cart_item.save()
        messages.info(request, f'{product.title} quantity increased!')

    return redirect('index')  # Повертаємось на головну сторінку
# Функція для перегляду корзини
def view_cart(request):
    session_id = request.session.session_key  # Отримуємо сесію користувача
    cart_items = Cart.objects.filter(session_id=session_id)  # Отримуємо всі товари в корзині для цієї сесії

    total = sum(item.total_price() for item in cart_items)  # Загальна сума
    cart_item_count = cart_items.count()  # Кількість товарів у корзині

    return render(request, 'cart.html', {
        'cart_items': cart_items, 
        'total': total,
        'cart_item_count': cart_item_count
    })

# Функція для оновлення кількості товару в корзині
def update_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    new_quantity = int(request.POST.get('quantity', 1))  # Отримуємо нову кількість з форми
    cart_item.quantity = new_quantity
    cart_item.save()

    return redirect('cart')

# Функція для видалення товару з корзини
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.delete()

    return redirect('cart')