from rest_framework.response import Response
from rest_framework import generics
from django.utils import timezone
import httpagentparser
from django.db import connection


class GetUserTime(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        get_user_time = timezone.now()
        get_user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        # host_name = request.META["HTTP_USER_AGENT"]
        # host_name_get = httpagentparser.detect(host_name)['os']['name']
        if get_user_ip:
            ip = get_user_ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        response = {'timestamp': get_user_time,
                    'hostname': request.get_host(),
                    'engine': connection.vendor,
                    'visitor ip': ip}
        return Response(response)
