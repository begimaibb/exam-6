from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.forms import GuestForm
from webapp.models import Guest
# from webapp.validate import guest_validate


def index_view(request):
    guests = Guest.objects.order_by('-created_date').filter(status="active")
    context = {"guests": guests}
    return render(request, "index.html", context)


def create_guest(request):
    if request.method == "GET":
        form = GuestForm()
        return render(request, "create.html", {"form": form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            text = form.cleaned_data.get("text")
            new_guest = Guest.objects.create(name=name, email=email, text=text)
            return redirect("index")
        return render(request, "create.html", {"form": form})


def update_guest(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "GET":
        form = GuestForm(initial={
            "name": guest.name,
            "email": guest.email,
            "text": guest.text
        })
        return render(request, "update.html", {"form": form})
    else:
        form = GuestForm(data=request.POST)
        if form.is_valid():
            guest.name = form.cleaned_data.get("name")
            guest.email = form.cleaned_data.get("email")
            guest.text = form.cleaned_data.get("text")
            guest.save()
            return redirect("index")
        return render(request, "update.html", {"form": form})


def delete_guest(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {"guest": guest})
    else:
        guest.delete()
        return redirect("index")

