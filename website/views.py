from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

# Create your views here.
def index(request):
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        contexto = {'msg':'Parabéns. Coloque seu e-mail e cadastre sua ideia.'}
        return render(request, 'login.html', contexto)

    return render(request,'index.html', contexto)

def sobre(request):
    ideias = Ideia.objects.all()
    # categoria = request.POST.get('terra_plana')
    # categoria_pessoa = Ideia.objects.filter(categorias).first()
    contexto = {
        'ideia': ideias
        # 'categoria': categoria_pessoa
    }
    return render(request,'sobre.html', contexto)

def login(request):
    if request.method == 'POST':
        email_form = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_form).first()
        print('Salve meu bom!')
        if pessoa is None:
            contexto = {
                'msg': 'Cadastre-se para criar uma ideia'
            }
            return render(request, 'index.html', contexto)
        else:
            contexto = {
                'pessoa': pessoa
            }
            return render(request, 'ideias.html', contexto)

    return render(request, 'login.html', {})

#Essa função é chamada no momento que o user clica no botao?
def cadastrar_ideias(request):
    contexto = {}
    if request.method == 'POST':
        email_pessoa = request.POST.get('email') # Essa linha pega o e-mail da pagina de cadastro?
        pessoa = Pessoa.objects.filter(email=email_pessoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa # Não entendi essa linha
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categorias = request.POST.get('categorias')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            print('aeeeee')

            return redirect('/sobre')

    return render(request, 'ideias.html', contexto)