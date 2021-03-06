# -*- coding: utf-8 -*-
import os

gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

#Change it if needed.
BASIC_URL='/'

DEBUG = False
TEMPLATE_DEBUG = DEBUG


SESSION_COOKIE_AGE=3600


ADMINS = (
     ('Dmitry E. Kislov', 'kisl_di@mail.ru'),
)

MANAGERS = ADMINS



####################Have to be deleted#######################
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': os.path.join(PROJECT_PATH,'mybase.db'),  # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
#}
##############################################################


#####################New version###############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'scidam_rhdday',         # Or path to database file if using sqlite3.
        'USER': 'scidam_rhdday',         # Not used with sqlite3.
        'PASSWORD': 'e22a819b',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                  # Set to empty string for default. Not used with sqlite3.
    }
}
################################################################


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Vladivostok'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


LANGUAGES = [
    ('en', 'English'),
    ('ru','Russian')
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '../../rhdday_media').replace('\\','/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL =BASIC_URL+'media/'


#DJANGO CMS RELATIVE PATH:
CMS_PAGE_MEDIA_PATH = 'cms'

CMS_PLACEHOLDER_CONF = {
    'mainpage.html service_photos': {
        "plugins": ['MainPageService']
    },
     'mainpage.html service_years': {
        "plugins": ['MainPageService']
    },                 
     'mainpage.html mainpagecontent': {
        "plugins": ['TextPlugin', 'PicturePlugin', 
                    'ViedoPlugin']
    },

    'gallery.html service_years': {
        "plugins": ['MainPageService']
    },                   
    'gallery.html service_gallery': {
        "plugins": ['GalleryService']
    },     
    'archive.html archive_service_years': {
        "plugins": ['GetArchiveYears']
    },    
    'archive.html archive_content': {
        "plugins": ['TextPlugin', 'PicturePlugin', 'VideoPlugin', 
                    'FilePlugin','GoogleMapPlugin']
    },  
    'common.html common_content': {
        "plugins": ['TextPlugin', 'LinkPlugin', 'PicturePlugin', 'VideoPlugin', 
                    'FilePlugin', 'GoogleMapPlugin']
    },                     
                        
}


#WYM_CLASSES=''
#WYM_STYLES=''
#WYM_STYLESHEET = getattr(settings, "WYM_STYLESHEET",  '"%s"' % cms_static_url('css/wymeditor.css'))



# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '../../rhdday_static').replace('\\','/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL =BASIC_URL+'static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    os.path.join(PROJECT_PATH, 'templates').replace('\\','/'),
    os.path.join(PROJECT_PATH, 'main/webs').replace('\\','/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jksd;fjwponbkajdwoieghowoei208gks923ignafkgj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'rhdday.urls'



TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #os.path.join(PROJECT_PATH, 'templates').replace('\\','/'),
    os.path.join(PROJECT_PATH, 'templates/mainrhd').replace('\\','/'),
)

CMS_PERMISSION = True

#Django cms templates
CMS_TEMPLATES = (
    ('mainpage.html', 'MainPage Template'),
    ('gallery.html', 'Gallery Template'),
    ('common.html', 'Common Page Template'),
    ('archive.html', 'Main Archive Template')

 )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    )


INSTALLED_APPS = (
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

#Django cms necessary modules
    'cms',
    'mptt', 
    'tagging',
    'menus',
    'south',
    'sekizai',
    
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
    #my local modules:    
    'rhdday.main',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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

