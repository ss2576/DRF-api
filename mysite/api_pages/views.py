from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from .models import Parameter
from .serializers import ItemListSerializer
from log_config.log_config import log




# Create your views here.

serial = ItemListSerializer()


class Errore404(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    
    def __str__(self):
        return '404'


class Errore400(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    
    def __str__(self):
        return '400'


class Errore415(APIException):
    status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    
    def __str__(self):
        return '415'


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ItemListSerializer


    def create(self, request, *args, **kwargs):
        req = self.request
        @log(req)
        def set_post(self, request, *args, **kwargs):
            if request.method == 'POST' and len(request.query_params) > 0:
                method = (request.query_params['method']).lower()
                if method == 'ping':
                    data = serial.get_data(request)
                    serializer_class = ItemListSerializer(data=data)
                    if serializer_class.is_valid():
                        serializer_class.save()
                        return Response(serializer_class.data)
                    else:
                        raise Errore415
                else:
                    raise Errore400
            else:
                raise Errore400
        return set_post(self, request, *args, **kwargs)


    def get_queryset(self, *args, **kwargs):
        req = self.request

        @log(req)
        def set_get(self, *args, **kwargs):
            raise Errore404

        return set_get(self, *args, **kwargs)
