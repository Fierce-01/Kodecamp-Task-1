from django.urls import path
from .views import home, about, contact

app_name = "home"

urlpatterns = [
    path('', home, name = 'homeview'),
    path('about/', about, name = 'aboutview' ),
    path('contact/', contact, name = 'contactview')
]
