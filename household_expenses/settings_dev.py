from .settings_common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガー設定
    'loggers': {
        'django': {
            'handler': ['console'],
            'level': 'INFO',
        },

        # expensesのロガー
        'expenses': {
            'handler': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers':{
        'console':{
            'level': 'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '¥t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}
