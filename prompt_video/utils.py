import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def get_media_path(media_type, file_name):
    return os.path.join(settings.MEDIA_ROOT, media_type, file_name)

def get_static_path(file_name):
    return os.path.join(settings.STATIC_ROOT, file_name)

def save_file(file):
    fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'videos'))
    fs.save(file.name, file)