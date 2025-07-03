from django.shortcuts import render
from .models import InscritoPernoite

# Create your views here.
def formIncricaoPernoite(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        vai_calebe = request.POST.get('vai_calebe')
        usercode = request.POST.get('usercode', '')
        ip_usado = request.META.get('REMOTE_ADDR', '')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        if vai_calebe == 'sim':
            vai_calebe = True
        else:
            vai_calebe = False
        
        # Aqui você pode salvar os dados no banco de dados ou processá-los como necessário
        # Exemplo: inscritoPernoite.objects.create(nome=nome, email=email, vai_calebe=vai_calebe)
        InscritoPernoite.objects.create(nome=nome, email=email, vai_calebe=vai_calebe, usercodeUsado=usercode, ip_usado=ip_usado, user_agent=user_agent)
        # InscritoPernoite.save()

        return render(request, 'sucesso.html', {'nome': nome})
    else:
        context = {
            'usercode': request.GET.get('uc', '')
        }
        return render(request, 'form-pernoite.html', context)