from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'result': 'Welcome to the Home Page!',
        'data': 'Welcome to the Home Page!',
    }    

    if request.method == 'POST':
        # Process any POST data if needed
        context['result'] = 'You submitted a POST request!'
        context['data'] = request.POST.get('data', 'No data provided')
        
    return render(request, 'home.html', context)