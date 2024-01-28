
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('',include('basicConcept.urls')),
    #path('',include('irisApp.urls')),
    path('',include('TelecomPrediction.urls')),
    path('admin/', admin.site.urls),
]
