from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout

def render(request, template):
    return render_to_response(template, context_instance=RequestContext(request))

def home(request):
	return redirect('/asistencia')

def entrar(request):
    
    if request.user.is_authenticated():
        return redirect('/')

    message = "Please log in below..."
    username = password = ''

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                message = "Your account is not active, please contact the site admin."
        else:
            message = "Your username and/or password were incorrect."

    return render_to_response('entrar.html', {'message':message, 'username': username})

def salir(request):
    logout(request)
    return redirect('/')