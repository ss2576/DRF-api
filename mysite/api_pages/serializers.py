from rest_framework import serializers
from .models import Parameter


class ItemListSerializer(serializers.HyperlinkedModelSerializer):
    def get_data(self, request):
        path_info = request.META['PATH_INFO']
        query_string = request.META['QUERY_STRING']
        data = {
            'parameter': f'{path_info}?{query_string}',
            'ip_addr': request.META['REMOTE_ADDR'],
        }
        return data

    class Meta:
        model = Parameter
        fields = ('id', 'parameter', 'ip_addr')


