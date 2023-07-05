from __future__ import annotations


def perm_gen_lex(string: str) -> list[str]:
    # TODO: implement me and remove this line of code
    if len(string) <= 1:
        return [string]

    perm_string = []
    for character in range(len(string)):
        simple_string = string[:character] + string[character + 1:]
        new_string = perm_gen_lex(simple_string)
        for items in new_string:
            perm_string.append(string[character] + items)
    return perm_string
