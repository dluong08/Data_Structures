from __future__ import annotations

# Add more imports here as you use functions from your hash table.
from hash_table import HashTable, insert, contains, get_item, keys
import string


def djbx33a(s: str) -> int:
    """Returns a modified DJBX33A hash of the given string.

    See the project specification for the formula.
    """
    n = min(len(s), 8)
    hash_value = 0
    for i in range(n):
        hash_value += ord(s[i]) * (33 ** (n - 1 - i))
    return 5381 * (33 ** n) + hash_value


def build_stop_words_table(stop_words_filename: str) -> HashTable:
    """Returns a hash table whose keys are the stop words.

    This will read the stop words from the file and add them to the stop
    words table.  The values stored in the table will not matter.

    Args:
        stop_words_filename: the name of the stop words file.

    Returns:
        A hash table whose keys are the stop words.
    """
    hash_table = HashTable(10, djbx33a)
    with open(stop_words_filename) as infile:
        for line in infile:
            token = line.split()
            for word in token:
                insert(hash_table, word, 0)
    return hash_table


def build_concordance_table(filename: str, stop_table: HashTable) -> HashTable:
    """Returns the concordance table for the given file.

    This will read the given file and build a concordance table
    containing all valid words in the file.

    Args:
        filename: the name of the file to read
        stop_table: a hash table whose keys are the stop words

    Returns:
        A concordance table built from the given file.
    """
    hash_table = HashTable(10, djbx33a)
    counter = 1
    with open(filename) as infile:
        for line in infile:
            i = line.lower()
            i = i.replace("\'", "")
            for j in string.punctuation:
                i = i.replace(j, " ")
            line_word = set(i.split())
            for word in line_word:
                if not contains(stop_table, word) and word.isalpha():
                    try:
                        insert(
                            hash_table, word, get_item(
                                hash_table, word) + (counter,))
                    except(KeyError):
                        insert(hash_table, word, (counter,))
            counter += 1
    return hash_table


def write_concordance_table(
        filename: str, concordance_table: HashTable) -> None:
    """Writes the concordance table to the given file.

    This will sort the strings in the concordance table alphabetically
    and write them to the given file along with the line numbers on
    which they occurred.

    Args:
        filename: the name of the file in which to store the table
        concordance_table: the concordance table
    """
    ordered_words = sorted(keys(concordance_table))
    infile = open(filename, "w")
    for word in ordered_words:
        infile.write(word + ': ')
        space = ""
        for i in get_item(concordance_table, word):
            space += str(i) + ' '
        space = space.rstrip()
        infile.write(space + '\n')
