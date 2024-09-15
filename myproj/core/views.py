from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email to your Gmail
            send_mail(
                f"New Contact Form Submission from {name}",
                f"Message: {message}\n\nFrom: {email}",
                'your-email@gmail.com',  # From email
                ['your-email@gmail.com'],  # To email
                fail_silently=False,
            )
            return redirect('success')  # Redirect to a success page after submission
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')