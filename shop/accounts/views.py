from django.contrib.auth.signals import user_logged_in
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Favorite
from listings.models import Listing


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("listings:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, template_name="accounts/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("listings:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, template_name="accounts/login.html", context={"login_form": form})


@login_required(login_url='/accounts/login/')
def account_info(request):
    return render(request, template_name="accounts/information.html")


def logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("listings:index")


@login_required(login_url='/accounts/login/')
def favoriteListings(request):
    user = request.user
    listings, created = Favorite.objects.get_or_create(user=user)
    context = {
        'listings': listings.listings.all(),
    }
    return render(request, template_name="accounts/favorite.html", context=context)


def deleteFavorite(request):
    item_id = request.POST.get('item')
    print(item_id)
    favorite = Favorite.objects.get(user=request.user)
    listing = Listing.objects.get(id=item_id)
    favorite.listings.remove(listing)
    favorite.save()
    return JsonResponse({'output': 'success'}, status=200)


def addFavorite(request):
    item_id = request.POST.get('item')
    favorite = Favorite.objects.get(user=request.user)
    listing = Listing.objects.get(id=item_id)
    messages.info(request, 'Dodano do ulubionych')
    favorite.listings.add(listing)
    favorite.save()
    return JsonResponse({'output': 'success'}, status=200)
