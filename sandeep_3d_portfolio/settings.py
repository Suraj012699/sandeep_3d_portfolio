import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-keep-it-safe')

# PRODUCTION mein DEBUG False hona chahiye, local ke liye True
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Render ka host add karna zaroori hai
ALLOWED_HOSTS = ['sandeep-3d-portfolio.onrender.com', 'localhost', '127.0.0.1', '*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', # staticfiles se pehle hona chahiye
    'django.contrib.staticfiles',
    'cloudinary',
    'gallery',
]

# ... baaki middleware aur templates wala section same rahega ...

# Database (Render par SQLite hi use ho raha hai filhal)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Cloudinary Configuration (Environment Variables use karna best hai)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'duelpvnfx'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '769979523652826'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', 'qkoNghah5s5tudCljl1d-Uhu2eU')
}

# Media files setup (Cloudinary ke liye)
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Static files setup
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')