from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import VehiculoForm, RegistroUsuarioForm
from .models import VehiculoModel
from urllib.parse import unquote
from tokenize import PseudoExtras
from django.views.generic import TemplateView, FormView

def indexView(request): 
    template_name = 'index.html'
    return render(request, template_name, {})

class AddVehiculoView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'http://127.0.0.1:8000/'
    permission_required = 'vehiculo.add_vehiculomodel'
    permission_denied_message = "No tienes permiso para agregar un vehículo."

    def get(self, request):
        form = VehiculoForm()
        return render(request, "addform.html", {'form': form})

    def post(self, request):
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehiculo agregado exitosamente.")
            return redirect('/')
        else:
            messages.error(request, "Datos incorrectos, no se pudo agregar el vehículo.")
            return render(request, "addform.html", {'form': form})

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('/')


""" def listVehiculo(request):
    template_name = 'lista.html'
    vehiculos = VehiculoModel.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, template_name, context) """

class ListVehiculoView(PermissionRequiredMixin, TemplateView):
    template_name = 'lista.html'
    permission_required = 'vehiculo.visualizar_catalogo'
    permission_denied_message = "Ingresa con tu cuenta para ver la lista de vehículos."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehiculos = VehiculoModel.objects.all()
        context['vehiculos'] = vehiculos
        context['marca_opts'] = {
            "1": "Ford",
            "2": "Fiat",
            "3": "Chevrolet",
            "4": "Toyota"
        }
        return context

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect('/vehiculo/login')

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            permission = Permission.objects.get(codename='visualizar_catalogo')
            user.user_permissions.add(permission)
            login(request, user)
            messages.success(request, "Registro Satisfactorio.")
            return HttpResponseRedirect('http://127.0.0.1:8000/')
        messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
    else:
        form = RegistroUsuarioForm()
    
    context = { "register_form" : form }
    return render(request, "registro.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste, sesión como: {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalido username o password.")
        else:
            messages.error(request, "Invalido username o password.")
            
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('http://127.0.0.1:8000/')