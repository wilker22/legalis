from django.conf import settings
from legalis import LEGALIS_APPS


def configure():
    if not settings.configured:

        test_settings = {
            'DATABASES': {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': ':memory:',
                },
            },
            'INSTALLED_APPS': LEGALIS_APPS,
            'TEMPLATE_CONTEXT_PROCESSORS': (
            ),
            'MIDDLEWARE_CLASSES': (
                'django.contrib.sessions.middleware.SessionMiddleware',
                'django.middleware.common.CommonMiddleware',
                'django.middleware.csrf.CsrfViewMiddleware',
                'django.contrib.auth.middleware.AuthenticationMiddleware',
                'django.contrib.messages.middleware.MessageMiddleware',
                'django.middleware.clickjacking.XFrameOptionsMiddleware',
                'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
            ),
            'HAYSTACK_CONNECTIONS': {
                'default': {
                    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
                }
            },
            'ROOT_URLCONF': 'tests.urls',
            'STATIC_URL': '/static/',
            'ADMINS': ('admin@example.com',),
            'DEBUG': False,
            'SITE_ID': 1,
        }

        settings.configure(**test_settings)
