import requests
from monitor.custom_timer import timer


@timer
def get_fibonacci(n):
    print(requests.get(f'http://127.0.0.1:5000/fibonacci?n={n}').status_code)


def monitor_fibonacci():
    for i in range(1000):
        get_fibonacci(i)


if __name__ == "__main__":
    monitor_fibonacci()
