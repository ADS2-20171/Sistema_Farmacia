from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)
SECRET_KEY = '1m$@y*ymmq(-k))5_*@az!-9*^1il0__&(7geq-24&1c48ybx-'

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
        'crispy_forms',
        'input_mask',

        'apps.main',
        'apps.users',
        'apps.cliente',
        'apps.compras',
        'apps.proveedor',
        'apps.ventas',
        'apps.medicamento',
        'apps.trabajador',
)

THIRD_PARTY_APPS = (

)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'farmacia.urls'


CRISPY_TEMPLATE_PACK = 'bootstrap3'


WSGI_APPLICATION = 'farmacia.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
