from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage 
from .forms import ContactForm

# Create your views here.

def contact(request):
    contact_form = ContactForm()
    # comprueba si se envia la informacion con method POST    
    if request.method == 'POST':
        # agrega un campo data con la información del diccionario con el method POST
        contact_form = ContactForm(data=request.POST)
        
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            sender_email = request.POST.get('email', '')  # Cambiado el nombre de la variable
            content = request.POST.get('content', '')

            # enviar un correo y redireccionar
            email_message = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto',
                f'De {name} <{sender_email}>\n\nEscribió\n\n{content}',
                'No contestar@inbox.mailtrap.io',
                ['yohander.diaz@gmail.com'],  # Cambiado a una lista de destinatarios
                reply_to=[sender_email]
            )

            try:
                email_message.send()
                # Algo no ha salido bien, redireccionamos a ok
                return redirect(reverse('contact') + "?ok")
            except Exception as e:
                # Imprimir detalles del error
                print(f"Error al enviar correo: {e}")
                # Algo no ha salido bien, redireccionamos el FAIL
                return redirect(reverse('contact') + "?fail")


    return render(request,'contact/contact.html', {'form':contact_form})