from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def auth_login(request):
	template_name = 'login.html'
	data = {}

	return render(request, template_name, data)


def auth_login(request):
	template_name = 'login.html'
	data = {}

	logout(request)

	username = password = ''

	#ALGUIEN PUSO EL BOTÓN ENVIAR
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		#VALIDACIÓN POR PARTE DE DJANGO
		user = authenticate(
			username=username,
			password=password
		)
		if user is not None:
			if user.is_active:
				if request.POST.get('remember_me', None):
					request.session.set_expiry(365)

				login(request, user)
				return HttpResponseRedirect(reverse('player_list'))
			else:
				messages.warning(
					request,
					'Usuario o contraseña incorrectos'
				)
		else:
			print("Usuario incorrecto")
			messages.error(
			request,
			'Usuario o contraseña incorrecto'
			)
	return render(request, template_name, data)


def auth_logout(request):
	logout(request)
	return HTTPResponseRedirect(reverse('player_list'))
