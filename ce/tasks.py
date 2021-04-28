# ce/taks.py
# Create your tasks here
from celery import shared_task
import time 

@shared_task
def add(x, y):
    delay = 5
    print("Process in {} second".format(delay))
    while delay != 0:
        delay -= 1
        time.sleep(1)
        print("time: {}".format(delay))
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
