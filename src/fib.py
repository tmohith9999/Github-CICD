def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number.
    Example: fibonacci(5) = 5
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
