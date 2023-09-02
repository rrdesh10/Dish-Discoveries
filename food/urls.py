from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:item_id>/', views.detail, name='detail'),  #detail view 
    path('add/', views.create, name='create'),  # add items
    path('update/<int:id>/', views.update, name='update'),  # update items
    path('delete/<int:id>/', views.delete, name='delete'),  # delete items
]