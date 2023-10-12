from django.shortcuts import render, get_object_or_404
from .models import Menu, MenuItem, SubMenuItem


# Функция для отображения меню.
def menu_view(request):
    # Получение всех объектов Menu из базы данных.
    menus = Menu.objects.all()
    menu_data = []

    # Для каждого меню, получаем связанные с ним верхние пункты меню (top_level_items).
    for menu in menus:
        top_level_items = MenuItem.objects.filter(menu=menu)
        menu_data.append((menu, top_level_items))

    context = {'menu_data': menu_data}
    return render(request, 'menu.html', context)


# Функция для отображения деталей пункта меню.
def menu_item_detail(request, item_id):
    # Получение объекта MenuItem с заданным идентификатором (item_id)
    item = get_object_or_404(MenuItem, id=item_id)
    menu = item.menu
    # Получение всех пунктов меню, связанных с тем же меню.
    menu_items = MenuItem.objects.filter(menu=menu)
    # Получение всех подпунктов меню (SubMenuItem), связанных с выбранным пунктом меню (item).
    subitems = SubMenuItem.objects.filter(parent_item=item)
    # Получение всех пунктов меню, связанных с тем же меню.
    related_menu_items = MenuItem.objects.filter(menu=menu)

    context = {
        'item': item,
        'menu': menu,
        'menu_items': menu_items,
        'subitems': subitems,
        'related_menu_items': related_menu_items,
    }
    return render(request, 'menu_item_detail.html', context)


# Функция для отображения деталей подпункта меню.
def subitem_detail(request, subitem_id):
    # Получение объекта SubMenuItem с заданным идентификатором (subitem_id)
    subitem = get_object_or_404(SubMenuItem, id=subitem_id)
    context = {'subitem': subitem}
    return render(request, 'subitem_detail.html', context)
