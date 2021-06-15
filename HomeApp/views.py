from django.shortcuts import render
from .forms import newsletter
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


def home(request):

    form_newsletter = newsletter()

    if request.method == 'POST':
        form_newsletter = newsletter(request.POST)

        if form_newsletter.is_valid():
            email = request.POST.get('email')

            html_content = render_to_string(
                'newsletters/newsletter.html', {'email': email})

            text_content = strip_tags(html_content)

            email = EmailMultiAlternatives('Gracias por suscribirte!!!', 'Mensaje: {}'.format(
                text_content), email, [email])

            email.attach_alternative(html_content, 'text/html')
            email.send()

    return render(request, 'home/home.html', {'newsletter': form_newsletter})
