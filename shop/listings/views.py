from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Listing, Category, Order, OrderListing
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.

def index(request):
    items = get_list_or_404(Listing.objects.all())
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories}
    return render(request, 'listings/index.html', context)


def listing(request, id):
    item = get_object_or_404(Listing, pk=id)
    return render(request, 'listings/listing.html', {'item': item})


def search(request):
    q = request.GET.get("q")
    items = Listing.objects.filter(name__icontains=q.strip())
    if "lastSearch" not in request.session or request.session['lastSearch']:
        request.session["lastSearch"] = [q]
        request.session.modified = True
    else:
        last_searches = request.session.get("lastSearch")
        last_searches.insert(0, q)
        request.session["lastSearch"] = last_searches[:3]
    return render(request, 'listings/search.html', {'items': items})


def quick_search(request):
    amount = 3
    if request.is_ajax() and request.method == "GET":
        text = request.GET.get('currentWord', None)
        items = list(Listing.objects.filter(name__icontains=text.strip())[:amount].values())
        return JsonResponse({"items": items}, status=200)
    return redirect('listings:index')


def category(request, id):
    items = Listing.objects.filter(category_id=id)
    return render(request, 'listings/category.html', context={'items': items})


def cart_view(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, finished=False)
    else:
        device = request.COOKIES['device']
        order, created = Order.objects.get_or_create(deviceId=device, finished=False)
    items = order.orderlisting_set.all()
    context = {'items': items, 'order': order}
    return render(request, 'listings/cart.html', context)


def update_cart_item(request):
    item_id = request.POST.get('item')
    action = request.POST.get('action')
    quantity = int(request.POST.get('quantity', 1))
    item = Listing.objects.get(id=item_id)
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, finished=False)
    else:
        device = request.COOKIES['device']
        order, created = Order.objects.get_or_create(deviceId=device, finished=False)

    orderItem, created = OrderListing.objects.get_or_create(listing=item, order=order)
    if action == "add":
        if not created:
            orderItem.quantity += quantity
    elif action == "delete":
        orderItem.quantity = 0
    else:
        # set
        orderItem.quantity = quantity
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    order.save()
    return JsonResponse({"output": "Done"}, status=200)
