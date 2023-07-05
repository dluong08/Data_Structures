def bears(n: int) -> bool:
    """Returns whether it is possible to win the bear game starting with
    n bears.
    
    Implemented recursively."""
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0 and bears(n // 2):
        return True
    if n % 5 == 0 and bears(n - 42):
        return True
    if n % 3 == 0 or n % 4 == 0:
        digit_1 = n % 10
        digit_2 = (n % 100) // 10
        return (digit_1 * digit_2 != 0) and bears(n - (digit_1 * digit_2))
    return False
