from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm,CustomerForm

# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_order = orders.count()
    delivered = orders.filter(status='delivered').count()
    pending = orders.filter(status='pending').count()


    context = {'orders':orders, 'customers': customers,'total_order':total_order,'delivered':delivered,'pending':pending}
    return render(request, 'home.html', context)

def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products':products})
    
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'customer.html', context) 

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'order_form.html', context)



def createCustomer(request):
    new_customer = CustomerForm()
    if request.method == 'POST':
        new_customer = CustomerForm(request.POST)
        if new_customer.is_valid():
            new_customer.save()
            return redirect('/')
    context = {'new_customer': new_customer}

    return render(request, 'customer_form.html', context)



def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'order_form.html', context)


def updateCustomer(request, pk):
    up_customer = Customer.objects.get(id=pk)
    update_customer = CustomerForm(instance=up_customer)
    if request.method == 'POST':
        update_customer = CustomerForm(request.POST, instance=up_customer)
        if update_customer.is_valid():
            update_customer.save()
            return redirect('/')
    context = {'update_customer': update_customer}

    return render(request, 'update_customer.html', context)



def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item':order}

    return render(request, 'delete.html', context)



def deleteCustomer(request,pk):
    delete_c = Customer.objects.get(id=pk)
    if request.method == 'POST':
        delete_c.delete()

        return redirect('/')

    context ={'delete_item': delete_c}

    return render(request, 'delete_user.html', context)