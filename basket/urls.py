from django.urls import path
from basket import views


urlpatterns = [
	path('', views.index, name="player"),
	path('list', views.index, name="player_list"),
	path('add/', views.add_player, name="player_add"),
	path('view/<int:player_id>', views.detail, name="player_detail"),
	#path('list2/', views.list2, name="player_list2"),
	#path('list2/<str:player_rut>', views.delete, name="player_delete"),
	#path('update/<str:player_rut>', views.update, name="player_update")
]