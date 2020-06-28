from decouple import config
from split_settings.tools import optional, include

ENV = config('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',
    'components/database.py',
    'components/emails.py',
    'components/rest_framework.py',

    f'environments/{ENV}.py',
    optional('environments/local.py')
]

include(*base_settings)
