class Pair:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __repr__(self) -> str:
        return 'Pair(%r, %r)' % (self.head, self.tail)

    def __eq__(self, other) -> bool:
        return (isinstance(other, Pair) and
                self.head == other.head and
                self.tail == other.tail)

def empty_list():
    return None

def add(lst: Pair, index: int, value) -> list:
    if index < 0 or index >= length(lst):
        raise IndexError
    if lst is None:
        return Pair(value, None)
    if index == 0:
        lst = Pair(value, lst)
        return lst
    return Pair(lst.head, add(lst.tail, index - 1, value))

def length(lst: Pair) -> int:
    if lst is None:
        return 0
    return 1 + length(lst.tail)

def get(lst: Pair, index: int):
    if index < 0 or lst is None:
        raise IndexError
    if index == 0:
        return lst.head
    return get(lst.tail, index - 1)

def setitem(lst: Pair, index: int, value):
    if index < 0 or lst is None:
        raise IndexError

    if index == 0:
        lst.head = value
        return lst
    return Pair(lst.head, setitem(lst.tail, index - 1, value))

def remove(lst: Pair, Index: int):
    if index < 0 or lst is None:
        raise IndexError
    if index == 0:
        value_return = lst.head
        return Pair(value_return, lst.tail)
    answer = remove(lst.tail, index - 1).head, Pair(lst.head,
                                                    remove(lst.tail,
                                                           index - 1).tail)
    return answer
