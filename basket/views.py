from django.shortcuts import render, redirect
from basket.models import Player, Coach, Team, Payroll
from basket.forms import PlayerForm, CoachForm, TeamForm, PayrollForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login')
def index(request):
	players = Player.objects.all().order_by('-id')
	data = {}

	# SELECT * FROM player
	#data['object_list'] = Player.objects.all().order_by('-id')

	data['object_list'] = players
	template_name = 'player/listar.html'

	return render(request, template_name, data)



def detail(request, player_id):

	data = {}
	template_name = 'player/detail_player.html'

	# SELECT * FROM player WHERE id = player_id
	data['player'] = Player.objects.get(pk=player_id)

	return render(request, template_name, data)



def delete(request,player_rut):
	p = Player.objects.get(rut=player_rut)
	p.delete()
	return redirect("player_list2")



def add(request):
	data = {}
	if request.method == "POST":
		data['form'] = PlayerForm(request.POST, request.FILES)

		if data['form'].is_valid():
			data['form'].save()

			return redirect('player_list')

	else:
		data['form'] = PlayerForm()


	template_name = 'player/agregar.html'
	return render(request, template_name,data)



def update(request,player_rut):
	data = {}
	player = Player.objects.get(rut=player_rut)
	if request.method == "GET":
		data['form'] = PlayerForm(instance=player)
	else:
		data['form']= PlayerForm(request.POST,request.FILES, instance=player)
		p = data['form']
		if p.is_valid():
			p.save()
		return redirect("player_list2")
	template_name = 'player/agregar.html'
	return render(request,template_name,data)



def list2(request):
	data = {}
	template_name = 'player/listar.html'
	data['list_player'] = Player.objects.all()

	return render(request, template_name,data)



def add_player(request):
	form = PlayerForm(request.POST, request.FILES)
	context = {'form':form}

	if request.method == "POST":
		print("if")

		if form.is_valid():
			form.save()
			return redirect('player_list')
	else:
		form = PlayerForm()
		print("else")
	
	template_name = 'player/agregar.html'
	return render(request, template_name, context)



def add_coach(request):
	form = CoachForm(request.POST, request.FILES)
	context = {'form':form}

	if request.method == "POST":
		print("if")

		if form.is_valid():
			form.save()
			return redirect('player_list')								#CAMBIAR
	else:
		form = CoachForm()
		print("else")
	
	template_name = 'coach/agregar.html'
	return render(request, template_name, context)



def add_team(request):
	form = TeamForm(request.POST, request.FILES)
	context = {'form':form}

	if request.method == "POST":
		print("if")

		if form.is_valid():
			form.save()
			return redirect('player_list')								#CAMBIAR
	else:
		form = TeamForm()
		print("else")
	
	template_name = 'team/agregar.html'
	return render(request, template_name, context)



def add_payroll(request):
	form = PayrollForm(request.POST)
	context = {'form':form}

	if request.method == "POST":
		print("if")

		if form.is_valid():
			form.save()
			return redirect('player_list')								#CAMBIAR
	else:
		form = PayrollForm()
		print("else")
	
	template_name = 'payroll/agregar.html'
	return render(request, template_name, context)