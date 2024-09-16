from config.env import env

# https://docs.celeryproject.org/en/stable/userguide/configuration.html

# CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='amqp://guest:guest@localhost//')
CELERY_RESULT_BACKEND = 'django-db'

CELERY_TIMEZONE = 'CET'

CELERY_BROKER_URL = "redis://redis:6379"
# CELERY_RESULT_BACKEND = "redis://redis:6379"

# CELERY_TIMEZONE = 'UTC'

# CELERY_TASK_SOFT_TIME_LIMIT = 20  # seconds
# CELERT_TASK_TIME_LIMIT = 30  # seconds
# CELERY_TASK_MAX_RETRIES = 3

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'