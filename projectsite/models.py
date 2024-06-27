from django.db import models
import django.utils.timezone as timezone

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=False)
    # You can add more fields if needed, like date_added, is_subscribed, etc.

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, default='')
    subject = models.CharField(max_length=200)
    message = models.TextField()
    dt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.subject

# SELECT * FROM contact_contactmessage; 


