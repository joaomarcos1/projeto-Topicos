from django.shortcuts import render, get_object_or_404,render_to_response, redirect
from .models import Pessoa, Curso, Funcao, StatusArtigo, Artigo, Noticia, Evento, Area, Aluno, Professor, horarios_laboratorio


from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from datetime import datetime


from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth


from .forms import RegistrationForm


# Create your views here.

def index(request):
	noticias = Noticia.objects.all().order_by('data_lancamento_noticia').reverse()
	return render (request, 'index.html', {'noticias':noticias})


def login_user(request):
	if (request.method == 'POST'):
		username = request.POST.get('username')
		password = request.POST.get('password')
		print (username)
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				if request.user.is_staff:
					return redirect('/admin')
				else:
					# Seleção radiobutton
					tipo_usuario = request.POST.get('optradio')
					if tipo_usuario == 'professor':
						return render(request, 'interface_professor.html')
					elif tipo_usuario == 'aluno':
						return render(request, 'interface_usuario.html')
					#return render(request, 'interface_usuario.html')
					#return redirect('/interface_usuario')
			else:
				return render(request, 'login.html', {'error_message': 'Sua conta nao esta ativa.'})
		else:
			return render (request, 'login.html', {'error_message': 'Login Inválido!'})
	return render (request,'login.html')



'''
def login_user(request):
	if (request.method == 'POST'):
		username = request.POST.get('username')
		password = request.POST.get('password')
		tipo_usuario = request.POST.get('optradio')
		if (tipo_usuario == "Sou Professor"):
			professor = Professor.objects.get(usuario=username, senha=password)
			return redirect ('/interface_professor/professor.id')
		if (tipo_usuario == "Sou Administrador"):
			render (request,'/admin')
	return render (request,'login.html')
'''



def artigos(request):
	artigos = Artigo.objects.all()
	return render (request, 'artigos.html', {'artigos':artigos})








def cadastro_em_evento(request, id):
    eventos = Evento.objects.all().filter(id=id)
   
    if (request.method == 'POST'):
    #    print("aaa")
    	Aluno.setEventoCadastrado(eventos)
    	Aluno.save
    return render(request, 'cadastro_em_evento.html', {'eventos':eventos})


def eventos(request):
	eventos = Evento.objects.all()
	return render (request, 'eventos.html', {'eventos':eventos})



def interface_professor(request, id):
	professor = Professor.objects.get(id = id)
	artigos = Artigo.objects.all()
	eventos = Evento,objects.all()
	noticias = Noticia.objects.all()
	return render (request, 'interface_professor.html', {'professor':professor, 'artigos':artigos, 'eventos':eventos, 'noticias':noticias})






def interface_usuario(request, pk=None):
	'''
	if not request.user.is_authenticaded():
		return redirect('/login')
		#return redirect('/interface_usuario/')
	else:
		if pk:
			user = User.objetcs.get(pk)
		else:
			user = request.user
			args = {'user': user}
			#args = request.user
			HttpResponseRedirect(request, 'interface_usuario.html', {'args':args})
	return render (request, 'interface_usuario.html')
'''
	if pk:
		user = User.objetcs.get(pk)
	else:
		user = request.user
		args = {'user': user}
			#args = request.user
		return render (request, 'interface_usuario.html', {'args':args})
	return render (request, 'interface_usuario.html')






def logout(request):
	auth.logout(request)
	return redirect('/')









def cadastro_usuario(request):
	form = RegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password1']
		password2 = form.cleaned_data['password2']
		if password != password2:
			return render(request, 'cadastro_usuario.html')
		elif first_name == '' or last_name == '' or email == '':
			return render(request, 'cadastro_usuario.html')
		user.set_password(password)
		user.save()

		if user is not None:
			if user.is_active:
				#return redirect('\interface_usuario')
				return render (request, 'interface_usuario.html')
	return render (request, 'cadastro_usuario.html', {'form':form})



def cadastro_artigo(request):
	artigos = Artigo()
	alunos = Aluno.objects.all()
	professores= Professor.objects.all()
	codigo = 0
	if(request.method == 'POST'):
		artigos.setTitulo(request.POST.get('titulo_Artigo'))
		artigos.setAutor(request.POST.get('autor_Artigo'))
		artigos.setCoautor(request.POST.get('coautor_Artigo'))
		artigos.setOrientador(request.POST.get('orientador_Artigo'))
		artigos.setStatus(request.POST.get('status_Artigo'))
		artigos.save()
		codigo = 1
		return render(request, 'cadastro_artigo.html', {'codigo':codigo, 'professores':professores, 'alunos':alunos})
	return render (request, 'cadastro_artigo.html', {'codigo':codigo, 'professores':professores, 'alunos':alunos})



def editar_perfil_alunos(request, id):
	alunos = Aluno.objects.get(id = id)
	codigo = 0
	if (request.method == 'POST'):
		alunos.setNome(request.POST.get('nome'))
		alunos.setMatricula(request.POST.get('matricula'))
		alunos.setCPF(request.POST.get('cpf'))
		alunos.setDataNascimento(request.POST.get('data_nascimento'))
		alunos.setCurso(request.POST.get('curso'))
		alunos.setUsuario(request.POST.get('username'))
		alunos.setSenha(request.POST.get('password'))
		alunos.save()
		codigo=1
	return render (request, "editar_perfil_aluno.html", {'alunos':alunos, 'codigo':codigo})




def entrada_saida_laboratorio(request):
	codigo = 0
	alunos = Aluno.objects.all()
	entrada = horarios_laboratorio()
	if (request.method == 'POST'):
		entrada.setAluno(request.POST.get('nome_aluno'))
		entrada.setHorarioEntrada(request.POST.get('data_inicio'))
		entrada.setHorarioSaida(request.POST.get('data_fim'))
		entrada.save()
		codigo = 1
		return render (request, 'entrada_saida_laboratorio.html', {'codigo':codigo, 'alunos':alunos})


	return render (request, 'entrada_saida_laboratorio.html', {'codigo':codigo, 'alunos':alunos})




def entradas_alunos(request):
	entradas = horarios_laboratorio.objects.all()
	return render (request, 'entradas_alunos.html', {'entradas':entradas})





def cadastro_aluno(request):
	aluno = Aluno()	
	codigo = 0
	if (request.method == 'POST'):
		aluno.setNome(request.POST.get('nome'))
		aluno.setMatricula(request.POST.get('matricula'))
		aluno.setCPF(request.POST.get('cpf'))
		aluno.setDataNascimento(request.POST.get('data_nascimento'))
		aluno.setCurso(request.POST.get('curso'))
		aluno.setUsuario(request.POST.get('username'))
		aluno.setSenha(request.POST.get('password'))
		aluno.save()
		codigo=1
		return render (request, 'cadastro_aluno.html', {'codigo':codigo})
	return render (request, 'cadastro_aluno.html', {'codigo':codigo})



def cadastro_professor(request):
	professor = Professor()
	codigo = 0
	if (request.method == 'POST'):
		professor.setUsuario(request.POST.get('username'))
		professor.setSenha(request.POST.get('password'))
		professor.setNome(request.POST.get('nome'))
		professor.setMatricula(request.POST.get('matricula'))
		professor.setCPF(request.POST.get('cpf'))
		professor.setDataNascimento(request.POST.get('data_nascimento'))
		professor.setCurso(request.POST.get('curso'))
		professor.setFuncao(request.POST.get('funcao'))
		professor.setEmail(request.POST.get('email'))
		professor.save()

		#ABAIXO - TESTE DE CRIAÇÃO DE USUÁRIO DO DJANGO COM AS MESMAS INFORMAÇÕES
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			username = request.POST.get('username')
			first_name = request.POST.get('nome')
			last_name = request.POST.get('nome')
			email = request.POST.get('email')
			password = request.POST.get('password')
			password2 = request.POST.get('password')
			if password != password2:
				return render(request, 'cadastro_professor.html')
			elif first_name == '' or last_name == '' or email == '':
				return render(request, 'cadastro_professor.html')
			user.set_password(password)
			user.save()
			
		codigo=1
		return render (request, 'cadastro_professor.html', {'codigo':codigo})

	return render (request, 'cadastro_professor.html', {'codigo':codigo})




def cadastro_evento(request):
	eventos = Evento()
	area = Area()
	codigo = 0
	if (request.method == 'POST'):
		eventos.setNomeEvento(request.POST.get('nome'))
		eventos.setArea(request.POST.get('area_Evento'))
		eventos.setDataInicioEvento(request.POST.get('data_inicio'))
		eventos.setDataFimEvento(request.POST.get('data_fim'))
		eventos.setQualis(request.POST.get('qualis_evento'))
		eventos.setLocal(request.POST.get('local'))
		eventos.setDescricao(request.POST.get('descricao_evento'))
		eventos.save()
		codigo = 1
		return render(request, 'cadastro_eventos.html', {'codigo':codigo})
	return render (request, 'cadastro_eventos.html', {'codigo':codigo})


def cadastro_noticias(request):
	noticia = Noticia()
	codigo = 0
	if (request.method == 'POST'):
		noticia.setTitulo(request.POST.get('titulo_noticia'))
		noticia.setCorpo(request.POST.get('corpo_noticia'))
		noticia.setImagem(request.POST.get('imagem_noticia'))
		noticia.setDataLancamentoNoticia(datetime.now())
		noticia.save()
		codigo = 1
		return render (request, 'cadastro_noticias.html', {'codigo':codigo})
	return render (request,'cadastro_noticias.html', {'codigo':codigo})


def noticia(request, id):
	noticia = Noticia.objects.get(id = id)
	return render(request, 'noticia.html', {'noticia':noticia})


def sobre(request):
    return render (request, 'sobre.html')
