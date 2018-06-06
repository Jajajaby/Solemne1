from django.shortcuts import render, redirect
from basket.models import Player, Coach, Team, Payroll
from basket.forms import PlayerForm, CoachForm, TeamForm, PayrollForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages



#LIST
@login_required(login_url='/auth/login')
def player_list(request):
	object_list = Player.objects.all().order_by('-id')				#LISTA DE JUGADORES
	paginator = Paginator(object_list, 3) 							#PARA MOSTRAR 3 JUGADORES POR PAGINA
	page = request.GET.get('page')									#PASA SABER QUÉ PÁGINA EN F(X) DE REGISTROS

	data = {}
	template_name = 'player/listar.html'

	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		p = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		p = paginator.page(paginator.num_pages)

	return render(request, template_name, {'object_list':object_list, 'p':p})


def team_list(request):
	object_list = Team.objects.all().order_by('-id')				#LISTA DE EQUIPOS
	paginator = Paginator(object_list, 3) 							#PARA MOSTRAR 3 EQUIPOS POR PAGINA
	page = request.GET.get('page')									#PASA SABER QUÉ PÁGINA EN F(X) DE REGISTROS

	data = {}
	template_name = 'team/listar.html'

	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		p = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		p = paginator.page(paginator.num_pages)

	return render(request, template_name, {'object_list':object_list, 'p':p})


def coach_list(request):
	object_list = Coach.objects.all().order_by('-id')				#LISTA DE ENTRENADORES
	paginator = Paginator(object_list, 3) 							#PARA MOSTRAR 3 ENTENADORES POR PAGINA
	page = request.GET.get('page')									#PASA SABER QUÉ PÁGINA EN F(X) DE REGISTROS

	data = {}
	template_name = 'coach/listar.html'

	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		p = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		p = paginator.page(paginator.num_pages)

	return render(request, template_name, {'object_list':object_list, 'p':p})


def payroll_list(request):
	object_list = Payroll.objects.all().order_by('-id')				#LISTA DE NOMINAS
	paginator = Paginator(object_list, 3) 							#PARA MOSTRAR 3 NOMINAS POR PAGINA
	page = request.GET.get('page')									#PASA SABER QUÉ PÁGINA EN F(X) DE REGISTROS

	data = {}
	template_name = 'payroll/listar.html'

	try:
		p = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		p = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		p = paginator.page(paginator.num_pages)

	return render(request, template_name, {'object_list':object_list, 'p':p})



#DELETE
def player_delete(request,id):
	p = Player.objects.get(id=id)

	if Player.objects.filter(id=id).exists():
		p = Player.objects.get(id=id)
		p.delete()
		#messages.add_message(request, messages.SUCCESS, "The player with id %s has been deleted" %id)
	else:
		print("No existe")
	
	return redirect('player_list')


def payroll_delete(request,id):
	p = Payroll.objects.get(id=id)

	if Payroll.objects.filter(id=id).exists():
		p = Payroll.objects.get(id=id)
		p.delete()
		#messages.add_message(request, messages.INFO, "The payroll with id %s has been deleted" %p)
	else:
		print("No existe")
	
	return redirect('payroll_list')


def coach_delete(request,id):
	p = Coach.objects.get(id=id)

	if Coach.objects.filter(id=id).exists():
		p = Coach.objects.get(id=id)
		p.delete()
		#messages.add_message(request, messages.SUCCESS, "The coach with id %s has been deleted" %id)
	else:
		print("No existe")
	
	return redirect('coach_list')


def team_delete(request,id):
	p = Team.objects.get(id=id)

	if Team.objects.filter(id=id).exists():
		p = Team.objects.get(id=id)
		p.delete()
		#messages.add_message(request, messages.SUCCESS, "The coach with id %s has been deleted" %id)
	else:
		print("No existe")
	
	return redirect('team_list')



#UPDATE
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
		return redirect('player_list')
	template_name = 'player/agregar.html'
	return render(request,template_name,data)


def payroll_update(request,id):
	data = {}
	payroll = Payroll.objects.get(id=id)
	if request.method == "GET":
		data['form'] = PayrollForm(instance=payroll)
	else:
		data['form']= PayrollForm(request.POST,request.FILES, instance=payroll)
		p = data['form']
		if p.is_valid():
			p.save()
		return redirect('payroll_list')
	template_name = 'payroll/agregar.html'
	return render(request,template_name,data)


def coach_update(request,id):
	data = {}
	coach = Coach.objects.get(id=id)
	if request.method == "GET":
		data['form'] = CoachForm(instance=coach)
	else:
		data['form']= CoachForm(request.POST,request.FILES, instance=coach)
		p = data['form']
		if p.is_valid():
			p.save()
		return redirect('coach_list')
	template_name = 'coach/agregar.html'
	return render(request,template_name,data)


def team_update(request,id):
	data = {}
	team = Team.objects.get(id=id)
	if request.method == "GET":
		data['form'] = TeamForm(instance=team)
	else:
		data['form']= TeamForm(request.POST,request.FILES, instance=team)
		p = data['form']
		if p.is_valid():
			p.save()
		return redirect('team_list')
	template_name = 'team/agregar.html'
	return render(request,template_name,data)



#ADD
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
			return redirect('coach_list')
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
			return redirect('team_list')

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
			return redirect('payroll_list')
	else:
		form = PayrollForm()
	
	template_name = 'payroll/agregar.html'
	return render(request, template_name, context)