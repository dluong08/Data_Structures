import unittest

from concordance import (
    build_stop_words_table, build_concordance_table, write_concordance_table)


class Tests(unittest.TestCase):
    def test_file1(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/file1.txt", stop_words)
        write_concordance_table("text_files/file1_con.txt", concordance_table)

        with open('text_files/file1_con.txt') as student_out, \
             open('text_files/file1_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_file2(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/file2.txt", stop_words)
        write_concordance_table("text_files/file2_con.txt", concordance_table)

        with open('text_files/file2_con.txt') as student_out, \
             open('text_files/file2_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_declaration(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/declaration.txt", stop_words)
        write_concordance_table(
            "text_files/declaration_con.txt", concordance_table)

        with open('text_files/declaration_con.txt') as student_out, \
             open('text_files/declaration_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_dictionary(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/dictionary_a-c.txt", stop_words)
        write_concordance_table(
            "text_files/dictionary_a-c_con.txt", concordance_table)

        with open('text_files/dictionary_a-c_con.txt') as student_out, \
             open('text_files/dictionary_a-c_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_war_and_peace(self) -> None:
        stop_words = build_stop_words_table("text_files/stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/war_and_peace.txt", stop_words)
        write_concordance_table(
            "text_files/war_and_peace_con.txt", concordance_table)

        with open('text_files/war_and_peace_con.txt') as student_out, \
             open('text_files/war_and_peace_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_file_the(self) -> None:
        stop_words = build_stop_words_table(
            "text_files/empty_stop_words.txt")
        concordance_table = build_concordance_table(
            "text_files/file_the.txt", stop_words)
        write_concordance_table(
            "text_files/file_the_con.txt", concordance_table)

        with open('text_files/file_the_con.txt') as student_out, \
             open('text_files/file_the_sol.txt') as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())


if __name__ == '__main__':
    unittest.main()
