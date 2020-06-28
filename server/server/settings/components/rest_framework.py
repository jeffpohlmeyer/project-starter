import datetime as dt


# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    )
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'REFRESH_TOKEN_LIFETIME': dt.timedelta(days=7),
    'ACCESS_TOKEN_LIFETIME': dt.timedelta(minutes=1)
}

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'auth/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'auth/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'user/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'EMAIL': {
        'activation': 'users.email.CustomActivationEmail',
    },
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_PASSWORD_RETYPE': True
}
