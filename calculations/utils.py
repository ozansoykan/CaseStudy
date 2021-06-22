from collections import deque

MAX_FOR_FACT = 100000
MAX_FOR_FIB = 100000
MAX_FOR_ACK_N = 100000


def validate_non_negative_int(arg):
    """
    Validates whether given args is a non-negative integer.

    :param arg: given arg to validate
    :raises ValueError: if argument is not o non-negative integer.
    """
    try:
        # Convert to int
        n = int(arg)
        # Check whether it was int (will fail if not int, e.g., 1.5 -> 1)
        if (str(n) if not isinstance(arg, int) else n) != arg:
            raise ValueError
    except ValueError:
        # Provided arg is not int -> Raise error
        raise ValueError(f"ERROR - Non integer argument provided: '{arg}'.")
    if n < 0:
        # Provided arg is a negative int -> Raise error
        raise ValueError(f"ERROR - Negative integer provided: '{arg}'.")
    return n


def validate_less_than_max(n, maxi, arg2=False):
    """
    Validates given value is not bigger than maximum.
    :param n: Value to check
    :param maxi: maximum value allowed
    :param arg2:
    :raises ValueError: if validation fails
    """
    if n > maxi:
        # Number is not within limits
        raise ValueError(
            f"ERROR - Please provide a positive integer less than {maxi} for {'arg2' if arg2 else 'arg1'}: '{n}'.")


def fib(n):
    """
    Calculates nth Fibonacci number.

    :param n: given number
    :return: calculation result
    :raises ValueError: if arg validation fails
    """
    # https://stackoverflow.com/questions/27194378/nth-fibonacci-number
    n = validate_non_negative_int(n)
    # Check whether number is within limits
    validate_less_than_max(n, MAX_FOR_FIB)
    n = n-1
    a, b = 0, 1
    count = 1
    while count <= abs(n):
        next_n = a + b
        a = b
        b = next_n
        count += 1
    return a


def fact(n):
    """
    Calculates nth factorial.
    :param n: given number
    :return: calculation result
    :raises ValueError: if arg validation fails
    """
    n = validate_non_negative_int(n)
    validate_less_than_max(n, MAX_FOR_FACT)
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def ack(m, n):
    """
    Calculates Ackermann(m,n).

    :param m: first number
    :param n: second number
    :return: calculation result
    :raises ValueError: if arg validation fails
    """
    m = validate_non_negative_int(m)
    n = validate_non_negative_int(n)
    if (m == 4 and n > 2) or m > 4 or n > MAX_FOR_ACK_N:
        raise ValueError(
            f"ERROR - Please provide args within limits: (arg1=4 and arg2<3) or (arg1<4 and arg2<={MAX_FOR_ACK_N}.")
    # https://rosettacode.org/wiki/Ackermann_function#Python:_Without_recursive_function_calls
    stack = deque([])
    stack.extend([m, n])

    while len(stack) > 1:
        n, m = stack.pop(), stack.pop()

        if m == 0:
            stack.append(n + 1)
        elif m == 1:
            stack.append(n + 2)
        elif m == 2:
            stack.append(2 * n + 3)
        elif m == 3:
            stack.append(2 ** (n + 3) - 3)
        elif n == 0:
            stack.extend([m - 1, 1])
        else:
            stack.extend([m - 1, m, n - 1])

    return stack[0]
