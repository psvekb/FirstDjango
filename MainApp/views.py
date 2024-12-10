from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item

author = {
    "name": "Сергей",
    "surname": "Владимирович",
    "lastname": "Пахомов",
    "mobile": "8-912-63-78-630",
    "email": "psv.ekb@gmail.com",
}


# Create your views here.
def home(request):
    context = {"name": "Пахомов Сергей Владимирович", "email": "psv.ekb@gmail.com"}
    return render(request, "index.html", context)


def about(request):
    context = author
    return render(request, "about.html", context)


def item(request, id):
    try:
        item = Item.objects.get(id = id)
        print(item)
        colors = item.colors.all()
        print(f'{colors=}')
        for color in colors:
            print(f'{color.name=}')
        context={"item": item, 'colors':colors}
        print(context)
        return render(request, "item.html", context)
    except:
        return HttpResponseNotFound(f'Товар c {id = } не найден')


def get_items(request):
    context={"items": Item.objects.all()}
    # print(context)
    return render(request, "items.html", context)
