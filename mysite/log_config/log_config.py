from datetime import datetime
from urllib.parse import unquote_plus
import os


def log(request):
    """
    декоратор для получения из функции переменной request
    и логгирования в файл.
    :param request:
    :return log_server:
    """
    def log_server(function):
        def called(*args, **kwargs):
            dict_param = get_dict_param(request)
            try:
                ret = function(*args, **kwargs)
                dict_param['status'] = str(ret.status_code)
            except Exception as e:
                dict_param['status'] = str(e)
            print(dict_param)
            write_to_file(dict_param)
            return function(*args, **kwargs)
        return called
    return log_server


def get_dict_param(request):
    """
    создание словаря {'time', 'url', 'method', 'status', 'params'}
    :param request:
    :return dict_param:
    """
    try:
        if request.META:
            path_info = request.META['PATH_INFO']
            query_string = request.META['QUERY_STRING']
            http_host = request.META['HTTP_HOST']
            request_method = request.META['REQUEST_METHOD']
            url = f'{http_host}{path_info}'
            dict_param = {
                'time': f'{datetime.now()}',
                'url': url,
                'method': request_method,
                'status': None,
            }
            if path_info == '/' and request_method == 'POST':
                dict_data = decode_dict(request)
                email = dict_data['email']
                dict_param['params'] = email
            elif path_info == '/api' and len(query_string) > 0:
                dict_param['params'] = query_string

    except Exception as e:
        print(f'{type(e).__name__}: {e}')
    return dict_param


def write_to_file(dict_param):
    """
    запись словаря dict_param в файл
    :param dict_param:
    :return:
    """
    ROOT = os.getcwd()
    DIRECTORY = os.path.join(ROOT)
    FILE = 'logfile.log'
    file = os.path.join(DIRECTORY, FILE)
    with open(file, 'a+', encoding='utf-8') as f:
        f.write(str(dict_param) + '\n')


def decode_dict(request):
    """
    декодирование переданных данных в словарь
    :param request:
    :return dict_data:
    """
    text_body = (request.body).decode('UTF-8')
    dict_data = {}
    if text_body:
        param = text_body.split('&')
        for item in param:
            k, v = item.split('=')
            v = unquote_plus(v)
            dict_data[k] = v
    return dict_data