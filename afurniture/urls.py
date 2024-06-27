from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from projectsite.views import home, products, new_arrivals, support, contact_success, our_partner, events, about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products', products, name='products'),
    path('new-arrivals', new_arrivals, name='new_arrivals'),
    path('contact-succes/', contact_success, name='contact_success'),
    path('our-partner', our_partner, name='our_partner'),
    path('events', events, name='events'),
    path('about-us', about_us, name='about_us'),
   path('support', support, name='support'),
    path('', include('projectsite.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)