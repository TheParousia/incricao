from django.shortcuts import render, get_object_or_404
from .models import InscritoPernoite, LinkCode

# Create your views here.
def formIncricaoPernoite(request):
    print(request.GET.get('uc', ''))
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        vai_calebe = request.POST.get('vai_calebe')
        camisa_calebe = request.POST.get('camisa_calebe')

        # datas_disponiveis = request.POST.get('datas_disponiveis', '') 
        
        datas_disponiveis = request.POST.getlist('datas_disponiveis')  # "meu_array[]" é o nome do campo no formulário

        if not datas_disponiveis:
            datas_disponiveis = None
        else:
            datas_disponiveis = ', '.join(datas_disponiveis)            

        observacao = request.POST.get('observacao', '')
        if observacao:
            observacao = observacao.strip()       

        print(datas_disponiveis)

        usercode = request.POST.get('usercode', '')
        usercode = usercode.strip()
        
        usercode = LinkCode.objects.filter(usercode=usercode).first()
            
        ip_usado = request.META.get('REMOTE_ADDR', '')
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        if vai_calebe == 'sim':
            vai_calebe = True
        else:
            vai_calebe = False
        
        if camisa_calebe == 'sim':
            camisa_calebe = True
        else:
            camisa_calebe = False
        # Aqui você pode salvar os dados no banco de dados ou processá-los como necessário
        # Exemplo: inscritoPernoite.objects.create(nome=nome, email=email, vai_calebe=vai_calebe)
        InscritoPernoite.objects.create(nome=nome, email=email, vai_calebe=vai_calebe, camisa_calebe=camisa_calebe, datas_disponiveis=datas_disponiveis, observacao=observacao, usercode_usado=usercode, ip_usado=ip_usado, user_agent=user_agent)
        # InscritoPernoite.save()

        return render(request, 'sucesso.html', {'nome': nome})
    else:
        usercode = request.GET.get('uc', '')
        print(f"Usercode recebido: {usercode}")
        usercode = get_object_or_404(LinkCode, usercode=usercode)
        
        context = {
            'usercode': usercode
        }
        return render(request, 'form-pernoite.html', context)