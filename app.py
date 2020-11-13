import time
import os
import redis

from flask import Flask

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')

if not redis_host:
    print("Provide REDIS_HOST environment variable")
    exit(1)

if not redis_port:
    print("Provide REDIS_PORT environment variable")
    exit(1)

cache = redis.Redis(host=redis_host, port=int(redis_port))


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)