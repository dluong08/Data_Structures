import sys
from array_stack_copy import ArrayStack, push, is_empty, pop

def tsort(edge_list: list[list[str]]) -> str:
    """Performs a topological sort of the given graph.

    The graph is specifed as a list of edges, where each edge is a list
    of two vertices.  The result will be a string formatted identically
    to the Unix utility tsort.  That is, a string with one vertex per
    line in topologically sorted order.

    For example:

    >>> print(tsort([['101', '202'], ['202', '203']]))
    101
    202
    203

    Args:
        edge_list: the graph to be topologically sorted, given as a list
            of edges.

    Returns:
        a string containing a topological ordering for the given graph

    Raises:
        ValueError:
            if the graph contains a cycle (isn't acyclic) with the
            message, "input contains a cycle"
    """
    lst = []
    for i in edge_list:
        for j in i:
            lst.append(j)
    out_str = ''
    lst_1 = {}
    lst_2 = []
    stack = ArrayStack(len(lst))
    for i in range(0, len(lst), 2):
        if lst[i] not in lst_1:
            lst_1[lst[i]] = [0, [], str(lst[i])]
            lst_2.append(lst[i])
        if lst[i + 1] not in lst_1:
            lst_1[lst[i + 1]] = [0, [], str(lst[i + 1])]
        lst_1[lst[i]][1].append(lst[i + 1])
        lst_1[lst[i + 1]][0] += 1
    for i in lst_2:
        if lst_1[i][0] == 0:
            push(stack, lst_1[i])
            del lst_1[i]
    while not is_empty(stack):
        v = pop(stack)
        for i in v[1]:
            lst_1[i][0] -= 1
            if lst_1[i][0] == 0:
                push(stack, lst_1[i])
                del lst_1[i]
        out_str += v[2] + '\n'
    if lst_1:
        raise ValueError('input contains a cycle')
    return out_str


# NOTE: You should not modify the main function.  You also don't need
# to write tests for the main function.
def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print('usage: python3 tsort <filename>', file=sys.stderr)
        sys.exit(1)

    with open(argv[1]) as file:
        edge_list = [line.split() for line in file]

    print(tsort(edge_list))


if __name__ == '__main__':
    main(sys.argv)
