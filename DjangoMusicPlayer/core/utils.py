from datetime import datetime
import os
import random


def song_path(instance, filename):
    _now = datetime.now()
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for _ in range(10))

    return 'songs/{year}/{month}/{day}/{basename}{randomstring}{ext}'.format(
        basename=basefilename, randomstring=randomstr, ext=file_extension,
        year=_now.strftime('%Y'), month=_now.strftime('%m'), day=_now.strftime('%d')
    )
