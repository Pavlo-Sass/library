from django.urls import path
from order import views as w_orders

urlpatterns = [
    path('', w_orders.index, name='orders'),
    path('create/', w_orders.create_order, name='create'),
    path('<int:order_id>', w_orders.get_order, name='user'),
    path('update/<int:order_id>/', w_orders.update_order, name='update'),
    path('delete/<int:order_id>', w_orders.delete_order),
]