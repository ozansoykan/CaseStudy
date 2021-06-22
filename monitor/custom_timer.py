import functools
import time


def timer(func):
    """
    Calculates time taken to run for the given function.

    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000
        print(f"--- {func.__name__} {args} -> {run_time:.3f} msecs")
        return value
    return wrapper_timer
