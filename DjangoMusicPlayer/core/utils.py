from datetime import datetime
import os
import random
from django.shortcuts import HttpResponse


def song_path(instance, filename):
    _now = datetime.now()
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for _ in range(10))

    return 'songs/{year}/{month}/{day}/{basename}{randomstring}{ext}'.format(
        basename=basefilename, randomstring=randomstr, ext=file_extension,
        year=_now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d')
    )


class APIAuthDecorator:
    def __init__(self, view_func):
        self.view_func = view_func

    def __call__(self, request, *args, **kwargs):
        if self.authenticate(request):
            return self.view_func(self, request, *args, **kwargs)
        else:
            return HttpResponse("Authentication failed", status=403)

    def authenticate(self, request):
        token = request.headers.get('USER', None)
        return token
