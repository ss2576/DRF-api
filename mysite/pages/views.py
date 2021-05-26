from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .models import Email
from urllib.parse import unquote_plus
from log_config.log_config import log



# Create your views here.


class Index:

    @staticmethod
    @csrf_exempt
    def index(request):

        @log(request)
        def get_post(request):
            if request.POST:
                assistant = Assistant()
                dict_data = assistant.decode_dict(request)
                email = dict_data['email']
                ip_addr = request.META['REMOTE_ADDR']
                if assistant.validateEmail(email):
                    data = {
                        'email': dict_data['email'],
                        'title': 'ваш e-mail',
                        'ip_addr': ip_addr,
                    }
                    model_email = Email()
                    model_email.save_object(data)
                    return render(request, 'email.html', context=data)
                else:
                    data = {
                        'title': 'ошибка отправки e-mail'
                    }
                    return render(request, 'error_email.html', context=data)

            else:
                data = {
                    'title': 'форма для отправки e-mail'
                }
                return render(request, 'index.html', context=data)

        return get_post(request)


class Assistant:

    @staticmethod
    def decode_dict(request):
        text_body = (request.body).decode('UTF-8')
        dict_data = {}
        if text_body:
            param = text_body.split('&')
            for item in param:
                k, v = item.split('=')
                v = unquote_plus(v)
                dict_data[k] = v
        return dict_data

    @staticmethod
    def validateEmail(email):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False