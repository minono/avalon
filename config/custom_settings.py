import sys
import os

from .default_settings import *

# =======================================
# custom settings
# =======================================

INSTALLED_APPS += ['avalon', 'channels']

# Add extra path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates')]

# DB 情報
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Time Zone
TIME_ZONE = 'Asia/Tokyo'

# 言語設定
LANGUAGE_CODE = 'ja'

# 静的ファイル
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)   # ファイルを置く場所
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")      # collectstatic で集まる場所
STATIC_URL = '/static/'                                  # 外部に向けた配信 URL

# channels の設定
ASGI_APPLICATION = 'config.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

# ログ設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'local': {
            'format': '\n%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d\n%(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'local',
        },
    },
    'loggers': {
        # コード中に明記したログ
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Djangoのエラー・警告・開発WEBサーバのアクセスログ
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 実行SQL
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
