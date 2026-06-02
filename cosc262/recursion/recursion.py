import numpy

def fast_exponentiation(a, n):
    """
    Returns a^n for integers
    :param a: an integer
    :param n: an integer
    :return: a^n for integers
    """

    if n == 0:
        return 1
    elif n % 2 == 0:
        p = fast_exponentiation(a, n / 2)
        return p * p
    else:
        return a * fast_exponentiation(a, n - 1)

def factorial(n):
    """
    Returns n! for integers
    :param n: an integer
    :return: n!
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fast_fibonacci(n):
    """
    Returns the nth fibonacci number
    :param n: an integer
    :return: the nth fibonacci number
    """

    I = [
        [1, 0],
        [0, 1]
    ]

    A = [
        [1, 1],
        [1, 0]
    ]

    def fib_mat(n):
        if n == 0:
            return I

        elif n % 2 == 0:
            p = fib_mat(n // 2)
            return matmul(p,p)

        else:
            p = fib_mat((n-1) // 2)
            return matmul(A, matmul(p,p))

    return fib_mat(n)[1][0]

def matmul(a, b):
    return (
        (
            a[0][0]*b[0][0] + a[0][1]*b[1][0],
            a[0][0]*b[0][1] + a[0][1]*b[1][1]
        ),
        (
            a[1][0]*b[0][0] + a[1][1]*b[1][0],
            a[1][0]*b[0][1] + a[1][1]*b[1][1]
        )
    )