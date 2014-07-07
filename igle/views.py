from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views.generic import View

def render(request, template):
    return render_to_response(template, context_instance=RequestContext(request))


class HomeView(View):
    """
    Esta es la vista de inicio del sitio web
    """

    def get(self, request, *args, **kwargs):
        
        if request.path == '/ipuc/':
            return redirect("/ipuc/asistencia")
        return redirect("/ipuc/")


class LoginView(View):
    """
    Esta vista ejecuta la funcionalidad de inicio de sesion en el sitio web
    """

    def get(self, request, *args, **kwargs):
        """
        Metodo GET en el request
        """

        if request.user.is_authenticated():
            return redirect('/')

        message = "Please log in below..."
        username = password = ''
        return render_to_response('entrar.html', {'message':message, 'username': username})

        
    
    def post(self, request, *args, **kwargs):
        """
        Metodo POST en el request
        """

        if request.user.is_authenticated():
            return redirect('/')

        message = "Please log in below..."

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


class LogoutView(View):
    """
    Esta vista ejecuta la funcionalidad de inicio de sesion en el sitio web
    """

    def get(self, request, *args, **kwargs):
        """
        Metodo GET en el request
        """

        logout(request)
        return redirect('/')