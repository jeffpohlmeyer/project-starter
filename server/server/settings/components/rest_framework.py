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
    'PASSWORD_RESET_CONFIRM_URL': 'user/password-reset/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'user/username-reset/{uid}/{token}',
    'ACTIVATION_URL': 'user/confirm/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'EMAIL': {
        'activation': 'users.email.CustomActivationEmail',
        'confirmation': 'users.email.CustomConfirmationEmail',
        'password_reset': 'users.email.CustomPasswordResetEmail',
        'password_changed_confirmation':
            'users.email.CustomPasswordChangedConfirmationEmail',
        'username_changed_confirmation':
            'users.email.CustomUsernameChangedConfirmationEmail',
        'username_reset': 'users.email.CustomUsernameResetEmail'
    },
    'USER_CREATE_PASSWORD_RETYPE': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'PASSWORD_RESET_CONFIRM_RETYPE': True,
    'USERNAME_RESET_CONFIRM_RETYPE': True
}
