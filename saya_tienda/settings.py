import os
from pathlib import Path

import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


def env_bool(name, default=False):
	value = os.getenv(name)
	if value is None:
		return default
	return value.strip().lower() in {"1", "true", "t", "yes", "y", "on"}


SECRET_KEY = os.getenv(
	"SECRET_KEY",
	"django-insecure-local-dev-key-change-me",
)

DEBUG = env_bool("DEBUG", default=False)

_default_hosts = "localhost,127.0.0.1,0.0.0.0,testserver"
# Railway injects RAILWAY_PUBLIC_DOMAIN automatically
_railway_domain = os.getenv("RAILWAY_PUBLIC_DOMAIN", "")
if _railway_domain:
	_default_hosts += f",{_railway_domain}"

ALLOWED_HOSTS = [*]
    
	


INSTALLED_APPS = [
	"django.contrib.admin",
	"django.contrib.auth",
	"django.contrib.contenttypes",
	"django.contrib.sessions",
	"django.contrib.messages",
	"django.contrib.staticfiles",
	"apps.games",
	"apps.interactions",
	"apps.users",
	
]

MIDDLEWARE = [
	"django.middleware.security.SecurityMiddleware",
	"whitenoise.middleware.WhiteNoiseMiddleware",
	"django.contrib.sessions.middleware.SessionMiddleware",
	"django.middleware.common.CommonMiddleware",
	"django.middleware.csrf.CsrfViewMiddleware",
	"django.contrib.auth.middleware.AuthenticationMiddleware",
	"django.contrib.messages.middleware.MessageMiddleware",
	"django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "saya_tienda.urls"

TEMPLATES = [
	{
		"BACKEND": "django.template.backends.django.DjangoTemplates",
		"DIRS": [BASE_DIR / "templates"],
		"APP_DIRS": True,
		"OPTIONS": {
			"context_processors": [
				"django.template.context_processors.request",
				"django.contrib.auth.context_processors.auth",
				"django.contrib.messages.context_processors.messages",
			],
		},
	},
]

WSGI_APPLICATION = "saya_tienda.wsgi.application"
ASGI_APPLICATION = "saya_tienda.asgi.application"


if env_bool("USE_SQLITE", default=False):
	DATABASES = {
		"default": {
			"ENGINE": "django.db.backends.sqlite3",
			"NAME": BASE_DIR / "db.sqlite3",
		}
	}
else:
	_db_url = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
	DATABASES = {
		"default": dj_database_url.config(
			default=_db_url,
			conn_max_age=600,
			# PyMySQL is installed as MySQLdb in __init__.py so dj-database-url
			# maps mysql:// → django.db.backends.mysql automatically.
		)
	}


AUTH_PASSWORD_VALIDATORS = [
	{
		"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
	},
	{
		"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
	},
]


LANGUAGE_CODE = "es-es"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STORAGES = {
	"default": {
		"BACKEND": "django.core.files.storage.FileSystemStorage",
	},
	"staticfiles": {
		"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
	},
}


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security settings — only enabled in production (DEBUG=False)
if not DEBUG:
	SECURE_SSL_REDIRECT = True
	SECURE_HSTS_SECONDS = 31536000
	SECURE_HSTS_INCLUDE_SUBDOMAINS = True
	SECURE_HSTS_PRELOAD = True
	SESSION_COOKIE_SECURE = True
	CSRF_COOKIE_SECURE = True
	SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
