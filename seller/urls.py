from django.urls import path
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.seller_index, name='seller_index'),
    path('add_food/', views.add_food, name='add_food'),  # 제품 등록 url
    path('food_detail/<int:pk>/', views.food_detail, name='food_detail'),  # 제품 상세 url
    path('food_delete/<int:pk>/', views.food_delete, name='food_delete'),  # 제품 삭제 url
]
