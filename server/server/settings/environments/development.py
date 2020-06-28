DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
    '[::1]'
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
