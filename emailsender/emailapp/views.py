from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from .utils.util import sendEmail

@csrf_exempt
def send_emails(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        password = request.POST.get('password')
        subject = request.POST.get('subject')
        text = request.POST.get('text')
        csv_file = request.FILES['csv']

        file_name = default_storage.save('uploaded_file.csv', csv_file)

        sendEmail(user_email, password, subject, text, file_name)

        return JsonResponse({'status': 'Emails sent'})
