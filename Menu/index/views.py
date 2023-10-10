from django.shortcuts import render, get_object_or_404
from .models import Menu, MenuItem



def menu_view(request):
    menus = Menu.objects.all()
    menu_data = []

    for menu in menus:
        top_level_items = MenuItem.objects.filter(menu=menu, parent_item__isnull=True)
        menu_data.append((menu, top_level_items))

    context = {'menu_data': menu_data}
    return render(request, 'menu.html', context)


def menu_item_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    subitems = MenuItem.objects.filter(parent_item=item)
    first_subitem = subitems.first() if subitems else None
    context = {'item': item, 'subitems': subitems, 'first_subitem': first_subitem}
    return render(request, 'menu_item_detail.html', context)
