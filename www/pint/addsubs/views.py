from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from signup import SignUpForm
from subtitles import MovieInformation
from django.contrib.auth.decorators import login_required


def index(request):
	context= {'user': request.user}
	return render(request,'addsubs/main.html',context)

@login_required()
def main(request):
	if request.POST.has_key('Path'):
		#user=
		path=request.POST['Path']
		# Comprobar con expresiones regulares si es una ruta
		# Comprobar si existe el video
		#video = algo sobre el path
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
	return render(request,'addsubs/main.html',context) # De momento redirecciona a la misma pagina, pero en un futuro redirigira a otra

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
