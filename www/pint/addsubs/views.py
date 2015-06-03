from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from signup import SignUpForm
from mencoder import Mencoder
from subtitles import Main
from django.contrib.auth.decorators import login_required
from addsubs.models import Movie
from addsubs.models import Job
import os.path
import threading

path = ""
job_id = ""
@login_required()
def main(request):
	context = {'error': None}
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
					return render(request,'addsubs/options.html',None) # Llevamos a las siguientes opciones
				else:
					context = {'error': 404}
	return render(request,'addsubs/main.html',context)

@login_required()
def options(request):
	font=size=delay=add=autoplay= None
	if job_id != "": # Si se entra directamente aunque se este logeado no hay trabajo que hacer
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
		t = threading.Thread(target = men.addsubs,args=(path,"addsubs.srt",font,size,delay,add,autoplay))
		t.start()
		#t.join()
		job.finished=True
		job.save
	context=None
	return redirect('main')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = User.objects.create_user(username=username, password=password)
			user.save()
			return redirect('main')
	else:
		form = SignUpForm()

	context={'form': form}
	return render(request,'addsubs/signup.html', context)

@login_required()
def jobs(request):
	job_list = Job.objects.filter(user=request.user)
	context = {'job_list':job_list}
	return render(request,'addsubs/jobs.html',context)
