"""
Django settings for CMM project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y+ouc)!dp@w$6$66b^yjdu729s98c*-9(yfz*14fw89y0rsr@t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CMM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'CMM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#여기있는 값들을 템플릿으로 전달한다. 일일히 뷰를 왔다가는것 보다는 효율적임
TEMPLATE_CONTEXT_PROCESSORS = (    
    #https://github.com/django/django/blob/1.10.5/django/contrib/auth/context_processors.py#L49
    "django.contrib.auth.context_processors.auth",     

    "django.core.context_processors.debug",    
    "django.core.context_processors.i18n",    
    "django.core.context_processors.media",    
    "django.core.context_processors.static",  
    "django.core.context_processors.tz",    
    "django.contrib.messages.context_processors.messages",    
    'django.core.context_processors.request',
    )

UPDATE_URL = '/account/mypage'

#기본 로그인 페이지 URL을 지정
#login_required 장식자 등에 의해서 사용 (views에 정의할것이고 로그아웃으면 아래 주소로 자동 이동)
LOGIN_URL = '/account' #로그인이 구현되어있는 경로 설정


#로그인 완료 후에 next 인자가 지정되면 해당 URL로 페이지 이동하지만
#next 인자가 없으면 여기 URL로 이동
LOGIN_REDIRECT_URL = '/index'


#로그아웃 완료 후에
# - next_page 인자가 지정되면 next_page URL 로 페이지 이동 (GET인자를 지칭)
# - next_page 인자가 없으면 LOGOUT_REDIRECT_URL이 지정되었을 경우 해당 URL로 이동 
# - next_page 인자가 지정되지 않고 LOGOUT_REDIRECT_URL이 None일 경우(즉 둘다 아닐때)
#   redirect를 수행하지 않고 'logon/logout.html' 템플릿을 렌더링
LOGOUT_REDIRECT_URL = None


#인증에 사용할 커스텀 User 모델 지정. '앱이름.모델명'
AUTH_USER_MODEL = 'login.MyUser'

