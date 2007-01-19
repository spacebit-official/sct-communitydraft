# Django settings for goimcommunity project.

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Herbert Poul', 'herbert.poul@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = 'djangotest'             # Or path to database file if using sqlite3.
DATABASE_USER = 'django'             # Not used with sqlite3.
DATABASE_PASSWORD = 'test'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/kahless/dev/python/diamanda/media/'

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=6&cv@*svpas38mz%h-5j7*&61zhkiuej%17@$hrf#$!37qylx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
#    'sphene.sphboard.middleware.PerformanceMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'sphene.community.middleware.GroupMiddleware',
)

ROOT_URLCONF = 'goimcommunity.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/kahless/dev/python/templates',
    '/home/kahless/dev/python/sitetemplates',

    '/home/kahless/dev/python/sphenecoll/templates',

    '/home/kahless/dev/python/diamandas/myghtyboard/templates',
    '/home/kahless/dev/python/diamandas/wiki/templates',
)

import sys
sys.path.append('/home/kahless/dev/python/diamanda/diamandas/')
sys.path.append('/home/kahless/dev/python/diamanda')
sys.path.append('/home/kahless/dev/python/sphenecoll')
sys.path.append('/home/kahless/dev/python/inosit')


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.flatpages',

    'django.contrib.admin',
    
    'goimcommunity.polls',
    'goimcommunity.leaguesystem',
    
    'sphene.community',
    'sphene.sphboard',

    'inosit.tracker',

    'wiki',
    'myghtyboard',

)


# RSS Settings
SITE_NAME = 'Diamanda Wiki !'
SITE_DESCRIPTION = 'A Diamanda Wiki Script'
SITE_NEWS_LINK = '/' # where links of the RSS feeds should point

# Anonymous perms Settings
ANONYMOUS_CAN_EDIT=True
ANONYMOUS_CAN_ADD=True
ANONYMOUS_CAN_VIEW=True
ANONYMOUS_CAN_SET_CURENT=False

# wiki config
WIKI_USE_PDF = False # 'htmldoc' - uses htmldoc , False - no PDF generation
# if set to nonFalse API KEY "search" will allow also "Search this site with google"
# requires pyGoogle, uses current SITE_ID domain name !!! example.com by default, change it to yours!
WIKI_GOOGLE_SEARCH_API = False

# myghtyboard config
ANONYMOUS_CAN_ADD_TOPIC=True
ANONYMOUS_CAN_ADD_POST=True
FORUMS_USE_CAPTCHA = False # should add topic/post use captcha image
MYGHTYBOARD_THEME='CrystalClear/' # theme = folder name in diamandas/myghtyboard/templates with ending slash
MYGHTYBOARD_LANG='english' # pointless for CrystalClear

# thumb CBC
SITE_IMAGES_DIR_PATH = '/home/kahless/dev/python/diamanda/media/images/'
SITE_IMAGES_SRC_PATH = '/site_media/images/'

# Other
USE_BANS = False # use WIkiBans to prevent baned from add/edit actions

