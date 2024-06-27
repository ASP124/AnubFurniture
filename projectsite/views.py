from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from .models import NewsletterSubscriber
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def subscribe_newsletter(request):
    is_subscribed = None  # Initialize the flag

    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if the email already exists in the database
        if NewsletterSubscriber.objects.filter(email=email).exists():
            is_subscribed = False  # Flag to indicate email is already registered
        else:
            # Save the email to the database
            subscriber = NewsletterSubscriber.objects.create(email=email, is_subscribed=True)

            # Send a confirmation email to the subscriber
            subject = 'Thank You for Subscribing to Anub Furnitures Newsletter!'
            message = '''Dear Subscriber,

I hope this email finds you well! On behalf of the entire team at Anub Furniture, I wanted to extend our heartfelt thanks for subscribing to our newsletter. We are thrilled to have you as a new member of our furniture family we want to express our gratitude for choosing to stay connected with us.

As a subscriber to Anub Furniture's newsletter, you will be among the first to receive updates on our latest furniture collections, exclusive promotions, and exciting offers. Whether you are looking to furnish your home, redecorate a space, or simply seek inspiration for your interior designs, our newsletter is designed to keep you informed and inspired.

Should you have any questions or need assistance, please don't hesitate to reach out to our customer support team at info@anubfurniture.com.

Thank you for your trust and support. We look forward to serving you and helping you create a living space that reflects your unique style and personality.

Best regards,
Anub Furniture'''

            from_email = 'padhaicareermatrix2@gmail.com'  # Replace with your email address
            send_mail(subject, message, from_email, [email], fail_silently=False)

            is_subscribed = True  # Flag to indicate successful subscription

        return JsonResponse({'is_subscribed': is_subscribed})

    return redirect('home.html')

def products(request):
    return render(request, 'products.html')

def new_arrivals(request):
    return render(request, 'new_arrivals.html')

def support(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Thank You for Contacting Us'
            message = 'Dear {},\n\nThank you for contacting us. We have received your message and will get back to you shortly.\n\nBest regards,\nAnub Furniture'.format(form.cleaned_data['name'])
            from_email = 'padhaicareermatrix2@gmail.com'  # Replace with your email address
            to_email = form.cleaned_data['email']
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            form = ContactForm()  # Create a new, empty form instance
            return redirect('contact_success')  # URL name for the success page
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')

def contact_success(request):
    return render(request, 'contact_success.html')

def our_partner(request):
    return render(request, 'our_partner.html')

def events(request):
    return render(request, 'events.html')

def about_us(request):
    return render(request, 'about_us.html')
