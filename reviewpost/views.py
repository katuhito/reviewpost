from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpRequest

def signupview(request):
    return render(request, 'signup.html', {'somedata':100})
