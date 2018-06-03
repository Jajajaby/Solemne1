from django.urls import path
from basket import views


urlpatterns = [
	path('', views.index, name="player"),
	path('list', views.index, name="player_list"),
	path('add_player/', views.add_player, name="player_add"),
	path('add_coach/', views.add_coach, name="coach_add"),
	path('add_team/', views.add_team, name="team_add"),
	path('add_payroll/', views.add_payroll, name="payroll_add"),
	path('player_delete/<str:id>', views.player_delete, name="player_delete"),
	path('update/<str:id>', views.player_update, name="player_update")
	#path('list2/', views.list2, name="player_list2"),
	#path('list2/<str:player_rut>', views.delete, name="player_delete"),
]