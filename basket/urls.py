from django.urls import path
from basket import views


urlpatterns = [
	#path('', views.index, name="player"),
	path('list_player', views.player_list, name="player_list"),
	path('list_team', views.team_list, name="team_list"),
	path('list_coach', views.coach_list, name="coach_list"),
	path('list_payroll', views.payroll_list, name="payroll_list"),
	path('add_player/', views.add_player, name="player_add"),
	path('add_coach/', views.add_coach, name="coach_add"),
	path('add_team/', views.add_team, name="team_add"),
	path('add_payroll/', views.add_payroll, name="payroll_add"),
	path('player_delete/<str:id>', views.player_delete, name="player_delete"),
	path('payroll_delete/<str:id>', views.payroll_delete, name="payroll_delete"),
	path('coach_delete/<str:id>', views.coach_delete, name="coach_delete"),
	path('team_delete/<str:id>', views.team_delete, name="team_delete"),
	path('update_player/<str:id>', views.player_update, name="player_update"),
	path('update_payroll/<str:id>', views.payroll_update, name="payroll_update"),
	path('update_coach/<str:id>', views.coach_update, name="coach_update"),
	path('update_team/<str:id>', views.team_update, name="team_update"),
	#path('list2/', views.list2, name="player_list2"),
	#path('list2/<str:player_rut>', views.delete, name="player_delete"),
]