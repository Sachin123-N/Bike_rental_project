from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import BikeForm
from .models import Bike


@login_required(login_url="login_url")
def create_order(request):
    template_name = 'bikeapp/create.html'
    form = BikeForm()
    if request.method == "POST":
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_order(request):
    template_name = 'bikeapp/show.html'
    orders = Bike.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


def update_order(request, pk):
    obj = Bike.objects.get(id=pk)
    form = BikeForm(instance=obj)
    if request.method == "POST":
        form = BikeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, 'bikeapp/create.html', context)


def cancel_order(request, pk):
    obj = Bike.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, 'bikeapp/confirmation.html')
