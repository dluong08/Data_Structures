def convert(num: int, base: int) -> str:
    """Returns a string representing num in the given base.
    Implemented recursively."""
    if num <= 1:
        return str(num)
    if num % base >= 10:
        if num % base == 10:
            return convert(num // base, base) + "A"
        if num % base == 11:
            return convert(num // base, base) + "B"
        if num % base == 12:
            return convert(num // base, base) + "C"
        if num % base == 13:
            return convert(num // base, base) + "D"
        if num % base == 14:
            return convert(num // base, base) + "E"
        if num % base == 15:
            return convert(num // base, base) + "F"
    return str(convert(num // base, base)) + str(num % base)
