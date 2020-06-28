import os
from split_settings.tools import optional, include

ENV = os.environ.get('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',
    'components/database.py',
    'components/emails.py',

    f'environments/{ENV}.py',
    optional('environments/local.py')
]

include(*base_settings)
