from django.contrib import admin
from .models import ContactMessage, NewsletterSubscriber

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name","subject","dt")
    list_filter = ("dt",)
    search_fields = ("name",)  

class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "is_subscribed")
    search_fields = ("email",)  # Add search functionality for email field

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(NewsletterSubscriber, NewsletterSubscriberAdmin)
