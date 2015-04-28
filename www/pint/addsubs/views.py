from django.shortcuts import render
from django.http import HttpResponse


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
