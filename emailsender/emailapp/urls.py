from django.urls import path
from django.views.static import serve
from django.conf import settings
from .views import send_emails

urlpatterns = [
    path('email_sender/send_emails/', send_emails),
    path('', serve, {'document_root': settings.STATICFILES_DIRS[0], 'path': 'emailapp/index.html'}),
]
