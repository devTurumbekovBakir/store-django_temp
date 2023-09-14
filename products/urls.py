from django.urls import path

from .views import products, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/delete/<int:basket_id>/', basket_delete, name='basket_delete'),
]
