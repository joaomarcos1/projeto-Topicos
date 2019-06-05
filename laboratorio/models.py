from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import re





class Curso(models.Model):
	curso = models.TextField()
	def __str__(self):
		return self.curso


class Funcao(models.Model):
	funcao = models.TextField()
	def __str__(self):
		return self.funcao

class StatusArtigo(models.Model):
	status = models.TextField()
	def __str__(self):
		return self.status







class Evento(models.Model):
	nome_evento = models.TextField(default='')
	data_inicio = models.DateTimeField()
	data_fim = models.DateTimeField()
	qualis = models.TextField(default='')
	area = models.TextField(default='')
	local = models.TextField(default='')
	descricao = models.TextField(default='')

	def setLocal(self, local):
		self.local = local
	def getLocal(self):
		return self.local

	def setDescricao(self, descricao):
		self.descricao = descricao
	def getDescricao(self):
		return self.descricao

	def setNomeEvento(self, nome_evento):
		self.nome_evento = nome_evento
	def getNomeEvento(self):
		return self.nome_evento

	def setDataInicioEvento(self, data_inicio):
		self.data_inicio = data_inicio
	def getDataInicioEvento(self):
		return self.data_inicio

	def setDataFimEvento(self, data_fim):
		self.data_fim = data_fim
	def getDataFimEvento(self):
		return self.data_fim

	def setQualis(self, qualis):
		self.qualis = qualis
	def getQualis(self):
		return self.qualis

	def setArea(self, area):
		self.area = area
	def getArea(self):
		return self.area


	def __str__(self):
		return self.nome_evento

		








class Aluno(models.Model):
	#username = models.CharField(max_length=50,unique=True,null=True)
	#password = models.CharField(max_length=50,null=True)
	#user = models.OneToOneField(User, on_delete = models.CASCADE)
	#usuario_u = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
	usuario = models.TextField(default='')
	senha = models.TextField(default='')
	matricula = models.TextField(default='')
	nome = models.CharField(max_length=50,null=True)
	cpf = models.IntegerField(null=True)
	#curso = models.ManyToManyField(Curso)
	#curso = models.ForeignKey(Curso, default=2, on_delete = models.CASCADE)
	curso = models.TextField(default='')
	#email = models.TextField()
	data_nascimento = models.TextField(max_length=20)
	#status = models.TextField()
	#funcao = models.ForeignKey(Funcao, default=2, on_delete = models.CASCADE)
	eventos_cadastrado = models.ManyToManyField(Evento)

	def setEventoCadastrado(self, eventos_cadastrado=''):
		self.eventos_cadastrado = eventos_cadastrado
	def getEventoCadastrado(self):
		return self.eventos_cadastrado


	def setCurso(self, curso):
		self.curso = curso
	def getCurso(self):
		return self.curso


	def setUsuario(self, usuario):
		self.usuario = usuario
	def getUsuario(self):
		return self.usuario

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(senha):
		return self.senha


	def setMatricula(self, matricula):
		self.matricula = matricula
	def getMatricula(self):
		return self.matricula

	def setNome(self, nome):
		self.nome = nome
	def getNome(self):
		return self.nome

	def setCPF(self, cpf):
		self.cpf = cpf
	def getCPF(self):
		return self.cpf


#	def setEmail(self, email):
#		self.email = email
#	def getEmail(self):
#		return self.email



	def setDataNascimento(self, data_nascimento):
		self.data_nascimento = data_nascimento
	def getDataNascimnto(self):
		return self.data_nascimento

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(self):
		return self.senha


	def __str__(self):
		return self.nome



class Professor(models.Model):
	#username = models.CharField(max_length=50,unique=True,null=True)
	#password = models.CharField(max_length=50,null=True)
	#usuario = models.OneToOneField(User, on_delete = models.CASCADE)
	usuario = models.TextField(default='')
	senha = models.TextField(default='')
	matricula = models.TextField()
	nome = models.CharField(max_length=50,null=True)
	cpf = models.IntegerField(null=True)
	#curso = models.ManyToManyField(Curso)
	#curso = models.ForeignKey(Curso, default=2, on_delete = models.CASCADE)
	curso = models.TextField(default='')
	email = models.TextField()
	data_nascimento = models.TextField(max_length=20)
	#status = models.TextField()
	#funcao = models.ForeignKey(Funcao, default=2, on_delete = models.CASCADE)
	funcao = models.TextField(default='')

	def setEmail(self, email):
		self.email= email
	def getEmail(self):
		return self.email


	def setCurso(self, curso):
		self.curso = curso
	def getCurso(self):
		return self.curso


	def setFuncao(self, funcao):
		self.funcao = funcao
	def getFuncao(self):
		return self.funcao

	def setUsuario(self, usuario):
		self.usuario = usuario
	def getUsuario(self):
		return self.getUsuario

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(senha):
		return self.senha


	def setMatricula(self, matricula):
		self.matricula = matricula
	def getMatricula(self):
		return self.matricula

	def setNome(self, nome):
		self.nome = nome
	def getNome(self):
		return self.nome

	def setCPF(self, cpf):
		self.cpf = cpf
	def getCPF(self):
		return self.cpf

	def setEmail(self, email):
		self.email = email
	def getEmail(self):
		return self.email

	def setDataNascimento(self, data_nascimento):
		self.data_nascimento = data_nascimento
	def getDataNascimnto(self):
		return self.data_nascimento



	def __str__(self):
		return self.nome


class horarios_laboratorio(models.Model):
	#aluno = models.ForeignKey(Aluno, on_delete = models.CASCADE)
	aluno = models.TextField(default='')
	hora_entrada = models.DateTimeField(default='')
	hora_saida = models.DateTimeField(default='')


	def setAluno(self, aluno=''):
		self.aluno = aluno

	def setHorarioEntrada(self, hora_entrada=''):
		self.hora_entrada = hora_entrada
	def setHorarioSaida(self, hora_saida=''):
		self.hora_saida = hora_saida





class Pessoa(models.Model):
	#username = models.CharField(max_length=50,unique=True,null=True)
	#password = models.CharField(max_length=50,null=True)
	user = models.OneToOneField(User, on_delete = models.CASCADE, default='')
	matricula = models.TextField(unique=True,null=False, default='')
	nome = models.CharField(max_length=50,null=True)
	cpf = models.IntegerField(unique=True,null=True)
	#curso = models.ManyToManyField(Curso)
	#curso = models.ForeignKey(Curso, default=2, on_delete = models.CASCADE)
	email = models.TextField()
	data_nascimento = models.TextField(max_length=20)
	status = models.TextField()
	#funcao = models.ForeignKey(Funcao, default=2, on_delete = models.CASCADE)
	funcao = models.TextField(default='')

	def setUserName(self, username):
		self.username = username
	def getUserName(self):
		return self.username

	def setPassword(self, password):
		self.password = password
	def getPassword(password):
		return self.password


	def setMatricula(self, matricula):
		self.matricula = matricula
	def getMatricula(self):
		return self.matricula

	def setnNome(self, nome):
		self.nome = nome
	def getNome(self):
		return self.nome

	def setCPF(self, cpf):
		self.cpf = cpf
	def getCPF(self):
		return self.cpf

	def setEmail(self, email):
		self.email = email
	def getEmail(self):
		return self.email

	def setDataNascimento(self, data_nascimento):
		self.data_nascimento = data_nascimento
	def getDataNascimnto(self):
		return self.data_nascimento

	def setSenha(self, senha):
		self.senha = senha
	def getSenha(self):
		return self.senha




	def __str__(self):
		return self.nome




class Artigo(models.Model):
	autor = models.ForeignKey(Professor, default=2, on_delete=models.CASCADE)
	titulo = models.TextField(default='')
	coautor = models.TextField(default='')
	#caoutor = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
	orientador = models.TextField(default='')
	status = models.ForeignKey(StatusArtigo, default=1, on_delete=models.CASCADE)
	#status = models.TextField(default='')

	def setAutor(self, autor):
		self.autor = autor
	def getAutor(self):
		return self.autor

	def setTitulo(self, titulo):
		self.titulo = titulo
	def getTitulo(self):
		return self.titulo

	def setCoautor(self, coautor):
		self.coautor = coautor
	def getCoautor(self):
		return self.coautor

	def setOrientador(self, orientador):
		self.orientador = orientador
	def getOrientador(self):
		return self.orientador

	def setStatus(self, status):
		self.status = status
	def getStatus(self):
		return self.status



	def __str__(self):
		return self.titulo




class Noticia(models.Model):
    autor = models.ForeignKey(Professor, default=1, on_delete = models.CASCADE)
    descricao = models.CharField(max_length=100, null=True)
    titulo = models.TextField()
    corpo = models.TextField()
    data_lancamento_noticia = models.DateTimeField(null=True)
    imagem = models.ImageField(upload_to='media')
    

    def setImagem(self, imagem=''):
        self.imagem = imagem

    def setTitulo(self, titulo=''):
        self.titulo = titulo
    def getTitulo(self):
        return self.titulo

    def setCorpo(self, corpo=''):
        self.corpo = corpo
    def getCorpo(self):
        return self.corpo

    def setDataLancamentoNoticia(self, data_lancamento_noticia=''):
        self.data_lancamento_noticia = data_lancamento_noticia
    def getDataLancamentoNoticia(self):
        return self.data_lancamento_noticia


    def __str__(self):
        return self.titulo



class Area(models.Model):
	area = models.TextField()

	def __str__(self):
		return self.area

