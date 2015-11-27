# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from unipath import Path
BASE_DIR = Path(__file__).ancestor(2)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_a^7l7!wq_7%0wi%a=lx249i4&-lbn&#z*44cjs(^8194+dgja'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRDPARTY_APPS = (
    'crispy_forms',
    'flat',
    'registration',
)

LOCAL_APPS = (
    'apps.alumnos',
    'apps.maestros',
    'apps.lineas',
)

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS +LOCAL_APPS


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

ROOT_URLCONF = 'Speeducation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Speeducation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TestSpeed',
        'USER': 'admin',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC PARA COSAS INTERNAS DEL PROYECTO
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR.child("static", "static_root")

STATICFILES_DIRS = [
    BASE_DIR.child("static"),
    #'/var/www/static/',
]

#MEDIA ES TO DO LO QUE EL USUARIO GUARDA EN LA PAGINA
#MEDIA PARA COSAS PARA EL USUARIO
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child("static", "media_root")

#VARIABLES DE CONFIGURACION PARA REDUX
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

#AUTH_USER_MODEL = 'maestros.Maestro'

CRISPY_TEMPLATE_PACK = 'bootstrap3' #<-- MOTOR DE TEMPLATES PARA CRISPY