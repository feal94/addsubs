from django.shortcuts import render
from django.http import HttpResponse
from signup import SignUpForm


def index(request):
	if request.POST.has_key('ruta'):
		#user=
		path=request.POST['ruta']
		# Comprobar con expresiones regulares si es una ruta
		# Comprobar si existe el video
		#video = algo sobre el path
		if request.POST.has_key('idioma'):
			language=request.POST['idioma']
			# Comprobar con expresiones regulares si es con el formato correcto
			job=Job(user=user,video=video,language=language,finished=False)
			job.save()
	#job_list=Job.objects.all()
	job_list = []
	context={'job_list':job_list}
	return render(request,'addsubs/index.html',context)

def main(request):
	return render(request,'main.html',context)

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

	data = {
		'form': form,
	}
	return render(request,'signup.html', data, context)
