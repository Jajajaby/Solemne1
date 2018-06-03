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



def player_delete(request,id):
	#p = Player.objects.get(rut=player_rut)
	p = Player.objects.get(id=id)
	print("PLAYER %s" %p)

	if Player.objects.filter(id=id).exists():
		print("IF")
		p = Player.objects.get(id=id)
		p.delete()
	else:
		print("No existe")
	#p = get_object_or_404(Player, id=rut)
    #p.delete()
    #messages.add_message(request, messages.SUCCESS, "The player with rut %s has been deleted" %player_rut)
    
	return redirect('/basket/')



def player_update(request,id):
	data = {}
	player = Player.objects.get(id=id)
	if request.method == "GET":
		data['form'] = PlayerForm(instance=player)
	else:
		data['form']= PlayerForm(request.POST,request.FILES, instance=player)
		p = data['form']
		if p.is_valid():
			p.save()
		return redirect('/basket/')
	template_name = 'player/agregar.html'
	return render(request,template_name,data)



def list2(request):
	data = {}
	template_name = 'player/listar.html'
	data['list_player'] = Player.objects.all()

	return render(request, template_name,data)



def add_player(request):
	form = PlayerForm(request.POST or None)
	context = {'form':form}

	if request.method == "POST":
		form = PlayerForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('player_list')
	else:
		form = PlayerForm()
	
	template_name = 'player/agregar.html'
	return render(request, template_name, context)



def add_coach(request):
	form = CoachForm(request.POST or None)
	context = {'form':form}

	if request.method == "POST":
		form = CoachForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('player_list')								#CAMBIAR
	else:
		form = CoachForm()
	
	template_name = 'coach/agregar.html'
	return render(request, template_name, context)



def add_team(request):
	form = TeamForm(request.POST or None)
	context = {'form':form}

	if request.method == "POST":
		form = TeamForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('player_list')								#CAMBIAR
	else:
		form = TeamForm()
	
	template_name = 'team/agregar.html'
	return render(request, template_name, context)



def add_payroll(request):
	form = PayrollForm(request.POST or None)
	context = {'form':form}

	if request.method == "POST":
		form = PayrollForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('player_list')								#CAMBIAR
	else:
		form = PayrollForm()
	
	template_name = 'payroll/agregar.html'
	return render(request, template_name, context)