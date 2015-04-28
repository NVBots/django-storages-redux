import os

MEDIA_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'storages'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

DEFAULT_FILE_STORAGE = 'backends.s3boto.S3BotoStorage'
AWS_IS_GZIPPED = True
SECRET_KEY = 'hailthesunshine'

DEFAULT_LIBCLOUD_PROVIDER = 'libcloud_local'

LIBCLOUD_DIR = os.path.join(MEDIA_ROOT, 'libcloud')
if not os.path.exists(LIBCLOUD_DIR):
    os.makedirs(LIBCLOUD_DIR)

LIBCLOUD_PROVIDERS = {
    'libcloud_local': {
        'type': 'libcloud.storage.types.Provider.LOCAL',
        'user': LIBCLOUD_DIR,
        'key': LIBCLOUD_DIR,
        'path': LIBCLOUD_DIR,
        'bucket': 'local'
    },
}
