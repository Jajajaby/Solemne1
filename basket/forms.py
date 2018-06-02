from django.forms import ModelForm
from basket.models import Player, Team, Coach, Payroll


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']


class TeamForm(ModelForm):
	class Meta:
		model = Team
		fields = ['name', 'description', 'logo']


class CoachForm(ModelForm):
	class Meta:
		model = Coach
		fields = ['rut', 'name', 'nickname', 'age', 'email']


class PayrollForm(ModelForm):
	class Meta:
		model = Payroll
		fields = ['name', 'date', 'time', 'team', 'coach']