from django.shortcuts import redirect, render
from .models import Listing
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.

def index(request):
    items = get_list_or_404(Listing.objects.all())
    context = {'items': items, }
    return render(request, 'listings/index.html', context)


def listing(request, id):
    item = get_object_or_404(Listing, pk=id)
    return render(request, 'listings/listing.html', {'item': item})


def search(request):
    q = request.GET.get("q")
    last_searches = []
    items = Listing.objects.filter(name__contains=q)
    if "lastSearch" not in request.session or not request.session['lastSearch']:
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
        items = list(Listing.objects.filter(name__contains=text)[:amount].values())
        return JsonResponse({"items": items}, status=200)
    return redirect('listings:index')
