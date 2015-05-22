from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from signup import SignUpForm
from subtitles import MovieInformation
from django.contrib.auth.decorators import login_required
import os.path


def index(request):
	context= {'user': request.user}
	return render(request,'addsubs/main.html',context)

@login_required()
def main(request):
	if request.POST.has_key('Path'):
		#user=
		path=request.POST['Path']
		# Comprobar con expresiones regulares si es una ruta
		if os.path.exists(path):
			if request.POST.has_key('Language'):
				language=request.POST['Language']
				# Comprobar con expresiones regulares si es con el formato correcto
				#job=Job(user='user',video='video',language='language',finished=False)
				#job.save()
				sub = MovieInformation(path, language)
				sub.main()
				#job_list=Job.objects.all()
				job_list = []
				context={'job_list':job_list}
				return render(request,'addsubs/options.html',context) # Llevamos a las siguientes opciones
	context= {'user': request.user}
	return render(request,'addsubs/main.html',context)

def options(request):
	if request.POST.has_key('Font'):
		font=request.POST['Font']
	if request.POST.has_key('Size'):
		size=request.POST['Size']
	if request.POST.has_key('Delay'):
		size=request.POST['Delay']
	if request.POST.has_key('Add'):
		size=request.POST['Add']
	if request.POST.has_key('Autoplay'):
		size=request.POST['Autoplay']
	#Llenamos las opciones que haya pasado el usuario
	#Ahora tendriamos que hacer uso de esta acciones para anadir los subtitulos con memcoder
	return render(request,'addsubs/options.html',context) # Llevamos a la misma pagina por ahora

def signup(request):
	if request.method == 'POST':  # If the form has been submitted...
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = User.objects.create_user(username=username, password=password)
			user.save()

			return HttpResponseRedirect(reverse('main'))  # Redirect after POST
	else:
		form = SignUpForm()

	context={'form': form}
	return render(request,'addsubs/signup.html', context)
