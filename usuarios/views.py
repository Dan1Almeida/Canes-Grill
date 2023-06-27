from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def cadastro(request):
    # print(f'Method: {request.method}')
    if request.method == 'POST':
        # print(f'POST: {request.POST}')

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
        # user.save
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
    return render(request,'dashboard.html')



def logout(request):
    auth.logout(request)
    print('Você desconectou')
    return redirect('index.htm')
