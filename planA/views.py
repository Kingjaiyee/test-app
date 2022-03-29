from rest_framework.response import Response
from rest_framework import generics
from django.utils import timezone
from django.db import connection


class GetUserTime(generics.ListAPIView):
    # call the GET endpoint to get user info
    def get(self, request, *args, **kwargs):
        # get the timezone of the user
        get_user_time = timezone.now()
        get_user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if get_user_ip:
            ip = get_user_ip.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        response = {'timestamp': get_user_time,
                    'hostname': request.get_host(),
                    'engine': connection.vendor,
                    'visitor ip': ip}
        return Response(response)
