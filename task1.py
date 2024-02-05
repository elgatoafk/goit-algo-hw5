from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    """caching_fibonacci Calculate the Fibonacci number for a given index using caching.


    :return: A function that takes an index and returns the Fibonacci number at that index.
    :rtype: Callable[[int], int]
    """
    f_cache = {}

    def fibonacci(fib_index: int) -> int:
        """fibonacci Calculate the Fibonacci number for a given index using caching.


        :param fib_index: The index of the Fibonacci number to calculate.
        :type n: int
        :return: Writes and returns number into cache dictionary
        :rtype: int
        """
        nonlocal f_cache  # making sure we can change enclosing dictionary
        if fib_index in f_cache:
            return f_cache[fib_index]
        if fib_index <= 1:  # base case
            f_cache[fib_index] = fib_index
            return f_cache[fib_index]

        f_cache[fib_index] = fibonacci(fib_index - 1) + fibonacci(fib_index - 2)
        return f_cache[fib_index]

    return fibonacci


# Functionality check
fib = caching_fibonacci()
print(fib(10))
print(fib(15))
