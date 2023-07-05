from __future__ import annotations

from typing import Optional


# NOTE: This must be iterative, not recursive.  You should *not* modify
# the input list in any way.
def max_iterative(lst: Optional[list[float]]) -> Optional[float]:
    """Returns the maximum value in the given list.
    
    If the given list is empty, returns None.  If the given list is
    None, raises a ValueError.
    """
    # if it is empty return None
    # setting variable value_1 to be the first item of given list
    #comparing the value_1 to values in given list and if it is
    #larger, it becomes a new value, returning largest value
    if lst == None:
        raise ValueError
    if lst == []:
        return None
    else:
        value = lst[0]
        for item in lst:
            if item > value:
                value = item
        return value
        

# NOTE: This must be iterative, not recursive.  You should *not* modify
# the input list in any way, it will return a new list.
def reverse_list_iterative(lst: Optional[list[float]]) -> list[float]:
    """Reverses the given list.

    If the given list is None, raises a ValueError.
    """
    #Raising a ValueError if given list is None (empty)
    #Creating a new list for items in given list can be placed into
    #Counter to keep track of place in given list
    #taking the item in the list starting at the end of the list and placing
    #it into the new list
    
    if lst == None:
        raise ValueError
    reversed_lst = []
    for item in lst:
        reversed_lst = [item] + reversed_lst
    return reversed_lst
    
        
# NOTE: This must be recursive, not iterative.  You should *not* modify
# the input list in any way, it will return a new list.
# NOTE: This will be inefficient, please never do this outside of this
# lab.
def reverse_list_recursive(lst: Optional[list[float]]) -> list[float]:
    """Reverses the given list.

    If the given list is None, raises a ValueError.
    """
    if lst == None:
        raise ValueError
    if len(lst) == 0:
        return lst
    return reverse_list_recursive(lst[1:]) + lst[:1] 

