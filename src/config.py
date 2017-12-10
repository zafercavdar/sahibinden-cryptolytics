import os

REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
JOB_QUEUE = os.environ.get('JOB_QUEUE')
JOB_STATUS_CHANNEL = os.environ.get('JOB_STATUS_CHANNEL')
LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
