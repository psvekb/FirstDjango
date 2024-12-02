from django.shortcuts import render
from django.http import HttpResponse

user = {
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
    #     text = f'<h1>"Изучаем django"</h1>\
    # <strong>Автор</strong>: <i>{user['lastname']} {user['name'][0]}.{user['surname'][0]}.</i>'
    #     return HttpResponse(text)
    context = {"name": "Пахомов Сергей Владимирович", "email": "psv.ekb@gmail.com"}
    return render(request, "index.html", context)


def about(request):
    text = f'Имя: <strong>{user["name"]}</strong><br>\
        Отчество: <strong>{user["surname"]}</strong><br>\
        Фамилия: <strong>{user["lastname"]}</strong><br>\
        телефон: <strong>{user["mobile"]}</strong><br>\
        email: <strong>{user["email"]}</strong>'
    return HttpResponse(text)


def item(request, id):
    text = f"Товар с {id=} не найден<br>"
    for item in items:
        if item["id"] == id:
            text = f'<strong>Карточка товара</strong><br>\
                id: <strong>{item["id"]}</strong><br>\
                Наименование: <strong>{item["name"]}</strong><br>\
                количество: <strong>{item["quantity"]}</strong><br>'
            break
    text += '<a href="/items">назад к списку товаров</a>'
    return HttpResponse(text)


def itemspage(request):
    text = f"<strong>Список товаров</strong> <br> <ol>"
    for item in items:
        text += f'<li>id: {item["id"]}, Наименование: {item["name"]}, количество: {item["quantity"]},\
            <a href="/item/{item["id"]}">страница товара</a></li>'
    text += "</ol>"
    return HttpResponse(text)
