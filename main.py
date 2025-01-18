def factorial(n):
    """This function returns the factorial of a given integer"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
