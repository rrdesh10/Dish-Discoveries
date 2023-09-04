from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path('', views.IndexItem.as_view(), name='index'), 
    path('<int:pk>/', views.DetailItem.as_view(), name='detail'),  #detail view 
    path('add/', views.CreateItem.as_view(), name='create'),  # add items
    path('update/<int:id>/', views.update, name='update'),  # update items
    path('delete/<int:id>/', views.delete, name='delete'),  # delete items
]