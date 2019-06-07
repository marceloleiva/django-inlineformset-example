from django.urls import path

from example.views import OrderListView, OrderCreateView, OrderUpdateView

app_name = 'example'
urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('create/', OrderCreateView.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
]
