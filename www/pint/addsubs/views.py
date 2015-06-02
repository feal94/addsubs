from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from signup import SignUpForm
from mencoder import Mencoder
from subtitles import Main
from django.contrib.auth.decorators import login_required
from addsubs.models import Movie
from addsubs.models import Job
import os.path

path = ""
job_id = ""
@login_required()
def main(request):
	if request.POST.has_key('Path'):
		global path
		path=request.POST['Path']
		# Comprobar con expresiones regulares si es una ruta
		if os.path.exists(path):
			if request.POST.has_key('Language'):
				language=request.POST['Language']
				# Comprobar con expresiones regulares si es con el formato correcto
				sub = Main(path, language)
				answer = sub.main()
				if answer != None:
					job = Job(user=request.user,video=answer,language=language,delay="0",play=False,finished=False)
					job.save()
					global job_id
					job_id=job.id
					context={'job':job}
					return render(request,'addsubs/options.html',context) # Llevamos a las siguientes opciones
	context= {'user': request.user}
	return render(request,'addsubs/main.html',context)

def options(request):
	font=size=delay=add=autoplay= None
	job = Job.objects.get(id=job_id)
	if request.POST.has_key('Font'):
		font=request.POST['Font']
	if request.POST.has_key('Size'):
		size=request.POST['Size']
	if request.POST.has_key('Delay'):
		delay=request.POST['Delay']
		job.delay = delay
	if request.POST.has_key('Add'):
		add=request.POST['Add']
	if request.POST.has_key('Autoplay'):
		job.play = True
		autoplay=request.POST['Autoplay']
	job.save
	men = Mencoder()
	men.addsubs(path,"addsubs.srt",font,size,delay,add,autoplay)
	job.finished=True
	job.save
	context=None
	return render(request,'addsubs/main.html',context) # Volvemos al principioo

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = User.objects.create_user(username=username, password=password)
			user.save()

			return HttpResponseRedirect(reverse('main'))
	else:
		form = SignUpForm()

	context={'form': form}
	return render(request,'addsubs/signup.html', context)

@login_required()
def jobs(request):
	job_list = Job.objects.get(user=request.user)
	context = {'job_list':job_list}
	return render(request,'addsubs/jobs.html',context)
