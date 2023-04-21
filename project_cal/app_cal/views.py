from django.shortcuts import render

# Create your views here.


def compound_interest(request):
    if request.method == 'POST':
        principal = float(request.POST['principal'])
        time = int(request.POST['time'])
        interest_rate = float(request.POST['interest']) / 100
        interest = principal * (1 + interest_rate)**time - principal
        return render(request, 'index.html', {'interest': interest})
    else:
        return render(request, 'index.html')