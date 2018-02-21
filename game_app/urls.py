from django.urls import path
from game_app import views


urlpatterns = [
    path('create/', views.game_create, name='gamecreate'),
    path('update/<int:game_id>/', views.game_update, name='gameupdate'),
    path('delete/<int:game_id>/', views.game_delete, name='gamedelete'),
    path('list/', views.game_list, name='gamelist'),
    path('detail/<int:game_id>/', views.game_detail, name='gamedetail'),
]


