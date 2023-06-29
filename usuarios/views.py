from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from churras.models import Prato

# Create your views here.

def cadastro(request):
    # print(f'Method: {request.method}')
    if request.method == 'POST':
        # print(f'POST: {request.POST}') ENTENDER FUNCIONAMENTOS

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if not nome.strip(): 
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        
        if not email.strip():
            print('O campo Email não pode ficar em branco')
            return redirect('cadastro')

        if senha != senha2 or not senha.strip() or not senha2.strip():
            print('As senhas não Correspondem')
            return redirect('cadastro')    

        if User.objects.filter(email=email).exists():
            print('E-mail ja cadastrado')
            return redirect('cadastro') 
           
        if User.objects.filter(username=nome).exists():
            print('Usuario ja cadastrado')
            return redirect('cadastro')    

        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save

        print('Usuario Cadastrado com Sucesso')     
        return redirect('login')
    
    return render(request,'cadastro.html')



def login(request):

    if request.method == 'POST':

        email = request.POST['email'].strip()
        senha = request.POST['senha'].strip()

        if email == " " and senha == " ":
            print('Campos Vazios')
            return redirect('login') 
        
        print(email, senha)

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')

            print('Usuário e/ou senha inválidos')
            return redirect('login')

    return render(request,'login.html')


def dashboard(request):
    if request.user.is_authenticated:
        pratos = Prato.objects.filter(publicado= True).order_by('date_prato')
        contexto = {'lista_pratos': pratos,}
        return render(request,'dashboard.html',contexto)
    
    return redirect('index')



def logout(request):
    auth.logout(request)
    print('Você desconectou')
    return redirect('index')


def cria_prato(request):
    if request.method == 'POST':
        nome_prato = request.POST['nome_prato']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']

        if not nome_prato: 
            print('O campo nome não pode ficar em branco')
            return redirect('cria_prato')
        
        if not ingredientes: 
            print('O campo nome não pode ficar em branco')
            return redirect('cria_prato')
        
        if not modo_preparo: 
            print('O campo nome não pode ficar em branco')
            return redirect('cria_prato')
        
        if not tempo_preparo: 
            print('O campo nome não pode ficar em branco')
            return redirect('cria_prato')
        
        if not rendimento: 
            print('O campo nome não pode ficar em branco')
            return redirect('cria_prato')
        
        if not categoria: 
            print('O campo nome não pode ficar em branco')
            return redirect('cria_prato')


    return render(request,'cria_prato.html')
