from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	if request.POST.has_key('ruta'):
		#user=
		path=request.POST['ruta']
		# Aqui se podria comprobar con expresiones regulares si es una ruta
		# Aqui comprobar si existe el video
		#video = algo sobre el path
		if request.POST.has_key('idioma'):
			language=request.POST['idioma']
			# Aqui se podria comprobar con expresiones regulares si es una ruta
			job=Job(user=user,video=video,language=language)
			# Aqui se podria comprobar con expresiones regulares si es con el formato correcto
			job.save()
	#job_list=Job.objects.all()
	job_list = []
	context={'job_list':job_list}
	return render(request,'addsubs/index.html',context)
