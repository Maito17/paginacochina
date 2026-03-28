import os  # <-- MOVIDO AQUÍ (Debe estar fuera de las comillas triples)
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

def env_bool(name, default=False):
    return os.environ.get(name, '1' if default else '0').strip().lower() in {
        '1', 'true', 'yes', 'on'
    }


SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'saya-tienda-local-dev-key-change-me-5hV1fR6kN3qL8zP2xT9mD4wY7cA'
)

DEBUG = env_bool('DJANGO_DEBUG', True)

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        'DJANGO_ALLOWED_HOSTS',
        'paginacochina-production.up.railway.app,localhost,127.0.0.1,.up.railway.app'
    ).split(',')
    if host.strip()
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
    'apps.games',
    'apps.interactions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'saya_tienda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'saya_tienda.wsgi.application'

# DATABASE
# Local runs with SQLite by default. Enable MySQL with USE_MYSQL=1
# or by providing MYSQLHOST/MYSQLDATABASE env vars in production.
USE_MYSQL = (
    os.environ.get('USE_MYSQL', '0') == '1'
    or bool(os.environ.get('MYSQLHOST'))
    or bool(os.environ.get('MYSQLDATABASE'))
)

if USE_MYSQL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('MYSQLDATABASE', 'nexus_game'),
            'USER': os.environ.get('MYSQLUSER', 'root'),
            'PASSWORD': os.environ.get('MYSQLPASSWORD', 'root'),
            'HOST': os.environ.get('MYSQLHOST', 'localhost'),
            'PORT': os.environ.get('MYSQLPORT', '3306'),
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
            },
            'CONN_MAX_AGE': 600,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# CAMBIO RECOMENDADO: Para que Railway maneje bien el CSS
STATIC_ROOT = BASE_DIR / 'staticfiles' 

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# settings.py

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        'DJANGO_CSRF_TRUSTED_ORIGINS',
        'https://paginacochina-production.up.railway.app,https://*.up.railway.app'
    ).split(',')
    if origin.strip()
]
# Permite que Django confíe en la cabecera enviada por el proxy de Railway
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if not DEBUG:
    SECURE_SSL_REDIRECT = env_bool('DJANGO_SECURE_SSL_REDIRECT', True)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = int(os.environ.get('DJANGO_SECURE_HSTS_SECONDS', '31536000'))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env_bool('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', True)
    SECURE_HSTS_PRELOAD = env_bool('DJANGO_SECURE_HSTS_PRELOAD', True)
