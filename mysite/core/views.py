from django.shortcuts import render
from .models import *
# Create your views here.
def index (request):
	livros = Livro.objects.all()
	if not livros:
		livros = None
		print("Hello")
	else:
		print("xau")
	return render(
		request,
		'index.html',
		{
			"Livros":livros,
		}
	)
