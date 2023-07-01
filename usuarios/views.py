from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from churras.models import Prato

# Create your views here.

def campo_vazio(campo):
    return not campo.strip()

def senha_nao_iguais(senha,senha2):
    return senha != senha2


def cadastro(request):
    # print(f'Method: {request.method}')
    if request.method == 'POST':
        # print(f'POST: {request.POST}') ENTENDER FUNCIONAMENTOS

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        if campo_vazio(nome):
            messages.error(request,"O campo nome não pode ficar em branco") 
            return redirect('cadastro')
        
        if campo_vazio(email):
            messages.error(request,"O campo Email não pode ficar em branco")
            return redirect('cadastro')

        if senha_nao_iguais(senha,senha2) or campo_vazio(senha) or campo_vazio(senha2):
            messages.error(request,"As senhas não Correspondem ou o Campos está vazio ")
            return redirect('cadastro')    

        if User.objects.filter(email=email).exists():
            messages.error(request,"E-mail já cadastrado")
            return redirect('cadastro') 
           
        if User.objects.filter(username=nome).exists():
            messages.error(request,"Usuário já cadastrado")
            return redirect('cadastro')    

        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save

        messages.error(request,"Usuário cadastrado com sucesso")     
        return redirect('login')
    
    return render(request,'cadastro.html')



def login(request):

    if request.method=='POST':

        email=request.POST['email']
        senha=request.POST['senha']

        if email == "" and senha == "":
            messages.error(request,"os campos Não podem ficar vazios")
            return redirect('login') 
        
        print(email, senha)

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                messages.success(request,"Login realizado com sucesso")
                return redirect('dashboard')

        messages.error(request,"Usuário/Senha Inválido")
        return redirect('login')

    return render(request,'login.html')


def dashboard(request):
    if request.user.is_authenticated:
        pratos = Prato.objects.filter(pessoa=request.user.id).order_by('date_prato')
        contexto = {'lista_pratos': pratos,}
        return render(request,'dashboard.html',contexto)
    
    messages.error(request,"Você não tem permissão para acessar a dashboard")
    return redirect('index')



def logout(request):
    auth.logout(request)

    messages.success(request,"Você se Desconectou")
    return redirect('index')


def cria_prato(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            nome_prato = request.POST['nome_prato']
            ingredientes = request.POST['ingredientes']
            modo_preparo = request.POST['modo_preparo']
            tempo_preparo = request.POST['tempo_preparo']
            rendimento = request.POST['rendimento']
            categoria = request.POST['categoria']
            foto_prato = request.FILES['foto_prato']
           
            user = get_object_or_404(User,pk=request.user.id)

            prato = Prato.objects.create(
                pessoa=user,
                nome_prato=nome_prato,
                ingredientes=ingredientes,
                modo_preparo=modo_preparo,
                tempo_preparo=tempo_preparo,
                rendimento=rendimento,
                categoria=categoria,
                foto_prato=foto_prato)
            prato.save()

            print('Prato criado com sucesso')
            return redirect('dashboard')  

        return render(request,'cria_prato.html')  
             
    print('Você não tem permissão!')
    return redirect('index')

     
