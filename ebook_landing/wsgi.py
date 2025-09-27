import os
import sys

path = '/home/strategichorizon/ebook_landing'  # Replace with your actual path
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ebook_landing.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()