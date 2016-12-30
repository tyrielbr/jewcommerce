""WSGI config for djangoecommerce projects comentários são válidos
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jewecommerce.settings")

application =  get_wsgi_application()