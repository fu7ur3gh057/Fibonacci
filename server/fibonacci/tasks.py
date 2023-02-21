from celery import shared_task
from celery.utils.log import get_task_logger


# Function for nth Fibonacci number
def Fibonacci(number):
    # Check if input is 0 then it will
    # print incorrect input
    if number < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif number == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif number == 1 or number == 2:
        return 1

    else:
        return Fibonacci(number - 1) + Fibonacci(number - 2)


@shared_task(name='fibonacci')
def fibonacci_task(data):
    number = data['number']
    return Fibonacci(number)
