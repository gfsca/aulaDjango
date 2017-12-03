from django.db import models

class Livro (models.Model):
	titulo = models.CharField(max_length = 50)
	numpag = models.CharField(max_length = 50)
	ano = models.CharField(max_length = 8)
	codigo = models.AutoField(primary_key = True, editable = False)
	editora = models.ForeignKey('Editora', on_delete = models.CASCADE)

	def __str__(self):
		return self.titulo

class Editora (models.Model):
	nome = models.CharField(max_length = 50)
	cnpj = models.CharField(primary_key = True,max_length = 14)


	def __str__(self):
		return self.nome