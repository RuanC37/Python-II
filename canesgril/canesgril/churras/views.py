from django.shortcuts import render

# Create your views here.
def index (request):
    dados = {'lista_pratos': 
        {
            '1':'Picanha',
            '2':'Pao De Alho',
            '3':'Costela',
            '4':'Contra File ao alho'
        }
    }
    return render(request, 'index.html', dados)

def churrasco(request):
    context ={'email':'canesgril@teste.com'}
    return render(request, 'churrasco.html', context)