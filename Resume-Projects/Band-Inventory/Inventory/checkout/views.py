from django.shortcuts import render, redirect, get_object_or_404
from .models import Checkout
from .forms import CheckoutForm
from instruments.models import Instrument  # Import the Instrument model
from students.models import Student  # Import the Student model


# Create your views here.

def checkout_index(request):
    checkouts = Checkout.objects.all()
    context = {
        'checkouts': checkouts,
    }
    return render(request, 'checkout/index.html', context)

def add_checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checkout:checkout_index')
    else:
        form = CheckoutForm()

    # Load data from related models (e.g., instruments and students)
    instruments = Instrument.objects.all()
    students = Student.objects.all()

    context = {
        'form': form,
        'instruments': instruments,
        'students': students,
    }

    return render(request, 'checkout/add_checkout.html', context)


def view_checkout(request, checkout_id):
    checkout = get_object_or_404(Checkout, pk=checkout_id)
    context = {
        'checkout': checkout,
    }
    return render(request, 'checkout/view_checkout.html', context)


def edit_checkout(request, checkout_id):
    checkout = get_object_or_404(Checkout, pk=checkout_id)
    if request.method == 'POST':
        form = CheckoutForm(request.POST, instance=checkout)
        if form.is_valid():
            form.save()
            return redirect('checkout:view_checkout', checkout_id=checkout_id)
    else:
        form = CheckoutForm(instance=checkout)
    context = {
        'form': form,
        'checkout': checkout,
    }
    return render(request, 'checkout/edit_checkout.html', context)

