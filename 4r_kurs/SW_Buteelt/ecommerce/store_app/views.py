from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Baraa, Angilal
import sqlite3 as sql


def show_store(request):
    baraa = Baraa.objects.all()
    category = Angilal.objects.all()
    return render(request, "store.html", {'products': baraa, 'categories': category})

def show_baraa_form(request):
    return render(request, "baraa.html")


def index(request):
    with sql.connect('db.sqlite3') as con:
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute('''
            SELECT *
            FROM store_app_baraa
            WHERE is_available=TRUE
            ORDER BY id DESC
            LIMIT 8
        ''')
        products = cur.fetchall()
        cur.execute('SELECT * FROM store_app_angilal')
        categories = cur.fetchall()
        products_count = len(products)

    context = { 
        "products": products,
        "categories": categories,
        "products_count": products_count
    }


    return render(request, "index.html", context)



def show_cart(request):
    return render(request, "cart.html")


def show_dashboard(request):
    return render(request, "dashboard.html")


def show_order_complete(request):
    return render(request, "order_complete.html")


def show_place_order(request):
    return render(request, "place-order.html")


def show_product_detail(request):
    return render(request, "product-detail.html")


def show_register(request):
    return render(request, "register.html")


def show_search(request):
    return render(request, "search-result.html")


def show_signin(request):
    return render(request, "signin.html")

def show_baraa(request):
    baraa = Baraa.objects.all()
    return render (request, 'baraa.html', {'baraa':baraa})

def show_category_products(request, slug):
    # try:
    #     category = Angilal.objects.all(id = id)
    # except:
    #     raise Http404("Category not found")
    category = get_object_or_404(Angilal, slug = slug)
    products = Baraa.objects.filter(angilal=category, is_available = True)
    categories = Angilal.objects.all()
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'product_count': products.count()
    }
    return render (request,'store.html', context)

