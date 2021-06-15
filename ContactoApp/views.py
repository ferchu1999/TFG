from django.shortcuts import render, redirect, HttpResponse
from .forms import formulario_contacto
from django.core.mail import send_mail, EmailMultiAlternatives
from ProyectoFinal.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.


def contacto(request):

    formulario = formulario_contacto()

    if request.method == 'POST':
        formulario = formulario_contacto(request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            tfno = request.POST.get('tfno')
            mensaje = request.POST.get('mensaje')

            html_content = render_to_string(
                'form_contacto/email_template.html', {'title': 'Test email', 'content': mensaje, 'email': email, 'tfno': tfno})

            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives('Mensaje de: ' + nombre, 'Nombre: {} \n Email: {} \n Tfno: {} \n Mensaje: {}'.format(
                nombre, email, tfno, text_content), email, ['ferranguillem8@gmail.com'])

            email.attach_alternative(html_content, 'text/html')
            email.send()

            messages.success(request, 'Mensaje enviado con éxito')
            try:

                return redirect('/contacto/?valido')

            except:
                messages.error(request, 'Ups! Ha ocurrido un error')
                return redirect('/contacto/?error')
        else:
            messages.error(request, 'Ups! Ha ocurrido un error')
            return redirect('/contacto/?error')

    return render(request, 'form_contacto/contacto.html', {'formulario': formulario})
