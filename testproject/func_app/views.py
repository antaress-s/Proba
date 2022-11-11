from django.http import HttpResponse
from func_app.duplicate.func import calc
from func_app.duplicate.func import delete_dup


def index(request):
    return HttpResponse(f"Поиск дубликатов,где True - является дубликатом, False - не является дубликатом {calc()}, "
                        f"Таблица после удаления найденных дубликатов {delete_dup()}")



