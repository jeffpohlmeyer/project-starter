from decouple import config


DEBUG = False

ALLOWED_HOSTS = [
    config('DOMAIN_NAME')
]

EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
