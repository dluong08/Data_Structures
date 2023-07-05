class ArrayList:
    def __init__(self, capacity: int = 1):
        self.items: list = [None] * capacity
        self.capacity = capacity
        self.size = 0

def empty_list() -> list:
    return ArrayList(0)

def add(lst: ArrayList, index: int, value) -> list:
    if index < 0 or index > lst.capacity:
        raise IndexError
    if lst.size == 0:
        lst.items = [value]
        lst.capacity += 1
    elif lst.capacity == lst.size:
        new_lst = [None] * (lst.capacity * 2)
        end = False
        for i in range(lst.capacity):
            if i == index:
                new_lst[i] = value
                end = True
            else:
                new_lst[i] = lst.items[i - 1]
        if end:
            new_lst[lst.capacity] = lst.items[lst.capacity - 1]
        else:
            new_lst[lst.capacity] = value
        lst.items = new_lst
        lst.capacity *= 2
    else:
        for i in range(lst.size - 1, index - 1, -1):
            lst.items[i + 1] = lst.items[i]
        lst.items[index] == value
    lst.size += 1
    return lst
    
def length(lst: ArrayList) -> int:
    return lst.size

def get(lst: list, index: int):
    if index < 0 or index >= lst.capacity:
        raise IndexError
    return lst.items[index]
            
def setitem(lst: ArrayList, index: int, value) -> list:
    if index < 0 or index >= lst.capacity:
        raise IndexError
    lst.items[index] = value
    return lst

def remove(lst: list, index: int) -> tuple:
    if index < 0 or index >= lst.capacity:
        raise IndexError
    value_return = lst.items[index]
    if lst.size == 1:
        lst.items[0] = None
    elif index == lst.size - 1:
        lst[index] = None
    else:
        for i in range(index, lst.size):
            lst.items[i] = lst.items[i + 1]
        lst[length(self, lst)] = None
    lst.size -= 1
    return (value_return, lst)
