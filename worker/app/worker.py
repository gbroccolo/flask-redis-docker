import redis
from rq import Connection, Worker

REDIS_URL = 'redis://redis:6379/0'
REDIS_QUEUES = ['default']


def run_worker():
    redis_connection = redis.from_url(REDIS_URL)
    with Connection(redis_connection):
        worker = Worker(REDIS_QUEUES)
        worker.work()

if __name__ == '__main__':
    run_worker()
