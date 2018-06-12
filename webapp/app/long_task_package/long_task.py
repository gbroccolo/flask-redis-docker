import time


def long_task(duration):
    time.sleep(duration)
    return {'task': True}
