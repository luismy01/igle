<<<<<<< HEAD
import os
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django settings for iglesoft project.

REPORT_URL = 'http://free.hostingjava.it/-iglesoft/report'
LOGIN_URL = '/login/'
=======

# Django settings for igle project.
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Luis Miguel', 'luismy01@gmail.com')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
<<<<<<< HEAD
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'iglesia',                      # Or path to database file if using sqlite3.
        'USER': 'iglesia',                      # Not used with sqlite3.
        'PASSWORD': 'iglesia',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

=======
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'igle_produccion',                      # Or path to database file if using sqlite3.
        'USER': 'igle_test',                      # Not used with sqlite3.
        #'PASSWORD': 'lm3&db#',                  # Not used with sqlite3.
        'PASSWORD': 'test',                  # Not used with sqlite3.
        'HOST': 'postgresql1.alwaysdata.com',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
        #'TEST_NAME': 'igle_test', # base de datos para pruebas unitarias con django
    }
}


###############################################
# Identificando la ruta del proyecto
###############################################
import os
RUTA_PROYECTO = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# Grappelli no esta soportado en alwaysdata ... por ahora
# GRAPPELLI_ADMIN_TITLE = 'IPUC Veinte de Julio Cartagena'

>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Bogota'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
<<<<<<< HEAD
LANGUAGE_CODE = 'en'
=======
LANGUAGE_CODE = 'en-us'
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

<<<<<<< HEAD
LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, "templates/personas/locale/"),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"

MEDIA_ROOT = os.path.join(PROJECT_DIR, "public/media/")
=======
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'public/media/')
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
<<<<<<< HEAD
STATIC_ROOT = os.path.join(PROJECT_DIR, "public/static/")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"

=======
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
<<<<<<< HEAD
    os.path.join(PROJECT_DIR, "static/"),
    #os.path.join(PROJECT_DIR, "public/static/"),

=======

    os.path.join(RUTA_PROYECTO,'public/media/'),
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(&amp;2_u&amp;^i*p%77%pkn(jp0_#@543(2ncp0%-)0^ndc#t@9d5mfp'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

<<<<<<< HEAD
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'igle.middleware.ChangeLaguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'django.middleware.common.CommonMiddleware',

    # dana las solicitudes jquery ajax
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
=======
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

<<<<<<< HEAD
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.request",
)

=======
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
ROOT_URLCONF = 'igle.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'igle.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
<<<<<<< HEAD
    '/home/luis/workspace/igle/templates',
)

INSTALLED_APPS = (
=======
    os.path.join(RUTA_PROYECTO,'templates'),
)

INSTALLED_APPS = (
    # Grappelli no esta soportado en alwaysdata ... por ahora
    # 'grappelli',
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
<<<<<<< HEAD
    #'tesoreria',
    'secretary',
    'personas',
=======
    #, 'tesoreria'
    'asistencia',
    # 'mockups',
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

<<<<<<< HEAD
=======

GOOGLE_SECRET_CLIENT_ID = "notasecret"


LOGIN_URL = "entrar"
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
