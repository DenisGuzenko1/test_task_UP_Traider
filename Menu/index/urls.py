from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu_view'),
    path('item/<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),
    path('subitem/<int:subitem_id>/', views.subitem_detail, name='subitem_detail'),
]
