from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from .forms import InstrumentForm
from .models import Instrument

# Create your views here.

# Home view for the "website"
def home_view(request):
    return render(request, 'instruments/home.html')

def sort_by_id(instrument):
    return instrument.id

def sort_by_type(instrument):
    return instrument.type.lower()

def sort_by_serial_num(instrument):
    return int(instrument.serial_num)

def sort_by_maker(instrument):
    return instrument.maker.lower()

def instrument_index(request):
    sort_by = request.GET.get('sort_by', 'id')
    reverse_sort = request.GET.get('reverse', 'false') == 'true'

    instruments = Instrument.objects.all()

    sorting_functions = {
        'id': sort_by_id,
        'type': sort_by_type,
        'serial': sort_by_serial_num,
        'maker': sort_by_maker,
    }

    sorting_function = sorting_functions.get(sort_by, sort_by_id)

    instruments = sorted(instruments, key=sorting_function, reverse=reverse_sort)

    context = {
        "instruments": instruments
    }

    return render(request, "instruments/index.html", context)

def add_instrument(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instruments:instrument_index')
    else:
        form = InstrumentForm()
    return render(request, 'instruments/add_instrument.html', {'form': form})

def view_instrument(request, instrument_id):
    instrument = get_object_or_404(Instrument, pk=instrument_id)
    return render(request, 'instruments/view_instrument.html', {'instrument': instrument})

def edit_instrument(request, instrument_id):
    instrument = get_object_or_404(Instrument, pk=instrument_id)
    if request.method == 'POST':
        form = InstrumentForm(request.POST, instance=instrument)
        if form.is_valid():
            form.save()
            return redirect('instruments:view_instrument', instrument_id=instrument_id)
    else:
        form = InstrumentForm(instance=instrument)
    return render(request, 'instruments/edit_instrument.html', {'form': form, 'instrument': instrument})

def delete_index(request):
    if request.method == 'POST':
        selected_instruments = request.POST.getlist('instrument_ids')

        if selected_instruments:
            selected_instruments = [int(id) for id in selected_instruments]
            Instrument.objects.filter(id__in=selected_instruments).delete()
            return redirect('instruments:instrument_index')

    instruments = Instrument.objects.all()

    context = {
        "instruments": instruments
    }

    return render(request, 'instruments/delete_index.html', context)
