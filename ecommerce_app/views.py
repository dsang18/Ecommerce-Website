from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import json

def home(request):
    All_categories = Product.objects.values_list('category',flat=True).distinct()
    All_products = []
    for i in (All_categories):
        products = Product.objects.filter(category=i)
        All_products.append(products)

    return render(request, 'ecommerce_app/home.html', {"All_products":All_products})

def about(request):
    return render(request, 'ecommerce_app/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email_id = request.POST.get('emailID', '')
        phone = request.POST.get('phone','')
        query = request.POST.get('queries','')
        contact = Contact(name=name, email=email_id, phone=phone, query=query)
        contact.save()
    return render(request, "ecommerce_app/contact.html")

def tracker(request):
    if request.method=="POST":
        order_id = request.POST.get('orderId','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        try: 
            order = Order.objects.filter(order_id = order_id, email=email, phone=phone)
            ord_status = OrderUpdate.objects.filter(order_id = order_id)
            updates = []
            for item in ord_status:
                updates.append({'text':item.update_desc,'time':item.timestamp.strftime('%d-%m-%Y')})
                response = json.dumps([updates, order[0].items_json], default=str)    
            return HttpResponse(response)
        
        except Exception as e:
            return HttpResponse('{}')

    return render(request, "ecommerce_app/tracker.html")

def search(request):
    query = request.GET.get('search')
    All_categories = Product.objects.values_list('category',flat=True).distinct()
    All_products = []
    for i in (All_categories):
        products = Product.objects.filter(category=i)
        prod = [item for item in products if matchQuery(query, item.desc, item.product_name, item.category, item.subcategory)]
        if len(prod)!=0:
            All_products.append(prod)

    return render(request, 'ecommerce_app/home.html', {"All_products":All_products})

def matchQuery(query, desc, name, cat, subcat):
    query = query.upper()
    desc = desc.upper()
    name = name.upper()
    cat = cat.upper()
    subcat = subcat.upper()
    if query in desc or query in name or query in cat or query in subcat:
        return True
    else:
        return False

def productView(request, input_id):
    product_details = Product.objects.filter(id = input_id)
    return render(request, "ecommerce_app/productView.html", {"product" :product_details[0], "discount":product_details[0].price*0.2})

def checkout(request):
    if request.method=="POST":
        itemsJSON = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        email_id = request.POST.get('emailID', '')
        phone = request.POST.get('phone','')
        address = request.POST.get('Address1','') + " " + request.POST.get('Address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zipcode = request.POST.get('zipcode','')
        amount = request.POST.get('totalAmount','')
        order = Order(items_json=itemsJSON, name=name, amount=amount, address=address, email=email_id, city=city, state=state, phone=phone, zipcode=zipcode)
        order.save()
        update = OrderUpdate(order_id = order.order_id, update_desc = "The Order has been Placed")
        update.save()
        return redirect("/shop/order-placed/"+str(order.order_id)+"/")
    return render(request, "ecommerce_app/checkout.html")

def order_placed(request, input_id):
    return render(request, "ecommerce_app/order_placed.html", {'id':input_id})
    