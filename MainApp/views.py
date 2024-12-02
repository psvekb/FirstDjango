from django.shortcuts import render
from django.http import HttpResponse

author = {
    "name": "Сергей",
    "surname": "Владимирович",
    "lastname": "Пахомов",
    "mobile": "8-912-63-78-630",
    "email": "psv.ekb@gmail.com",
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


# Create your views here.
def home(request):
    context = {"name": "Пахомов Сергей Владимирович", "email": "psv.ekb@gmail.com"}
    return render(request, "index.html", context)


def about(request):
    # text = f'Имя: <strong>{user["name"]}</strong><br>\
    #     Отчество: <strong>{user["surname"]}</strong><br>\
    #     Фамилия: <strong>{user["lastname"]}</strong><br>\
    #     телефон: <strong>{user["mobile"]}</strong><br>\
    #     email: <strong>{user["email"]}</strong>'

    context = author

    return render(request, "about.html", context)


def item(request, id):
    text = f"Товар с {id=} не найден<br>"
    for item in items:
        if item["id"] == id:
            context = {
                "id": item["id"],
                "not_found": False,
                "name": item["name"],
                "quantity": item["quantity"],
            }

            return render(request, "item.html", context)

    context = {
        "id": id,
        "not_found": True,
    }

    return render(request, "item.html", context)


def itemspage(request):
    # context = {"items": items}
    return render(request, "items.html", context={"items": items})
