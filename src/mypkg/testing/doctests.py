#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the "doctests" example module.

This module shows some examples of the doctests in Python. 

Background Material:

* [How To Write Doctests in Python](https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python)
* [Doctest Documentation](https://docs.python.org/3/library/doctest.html)

Example:
    >>> factorial(5)
    120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    Args:
        n (int): argument of the factorial function.

    Returns:
        The factorial of the argument.


    Examples:
        Some basic example usages of the factorial function.

        >>> [factorial(n) for n in range(6)]
        [1, 1, 2, 6, 24, 120]
        >>> factorial(30)
        265252859812191058636308480000000
        >>> factorial(-1)
        Traceback (most recent call last):
            ...
        ValueError: n must be >= 0

        Factorials of floats are OK, but the float must be an exact integer:
        >>> factorial(30.1)
        Traceback (most recent call last):
            ...
        ValueError: n must be exact integer
        >>> factorial(30.0)
        265252859812191058636308480000000

        It must also not be ridiculously large:
        >>> factorial(1e100)
        Traceback (most recent call last):
            ...
        OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word.

    Args:
        word (string): Input word

    Returns:
        Nimber of vowels in the input word.

    Examples:

        >>> count_vowels('Cusco')
        2

        >>> count_vowels('Manila')
        3

        >>> count_vowels('Istanbul')
        3
    """
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels


if __name__ == "__main__":
    import doctest
    doctest.testmod()