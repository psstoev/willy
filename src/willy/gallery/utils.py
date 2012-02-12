import hashlib
import os
from datetime import datetime

from django.conf import settings

def save_picture(user, uploaded_file):
    sha = hashlib.sha1()

    message = '_'.join([user.username, uploaded_file.name, str(datetime.now())])
    extension = uploaded_file.name.split('.')[-1]
    file_name = hashlib.sha1(message).hexdigest() + '.' + extension
    full_name = os.path.join(settings.MEDIA_ROOT, settings.USER_FILES_DIR, file_name)
    
    picture = open(full_name, 'a')
    for chunk in uploaded_file.chunks():
        picture.write(chunk)
    picture.close()

    return full_name
