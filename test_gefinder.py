import unittest
import gefinder



class MyTestCase(unittest.TestCase):

    def test_status_report(self):

        status_1 = "\n\n*** Start sequence initiated ***\n\n*** Now retrieving data... ***"
        status_2 = "\n*** Data received successfully ***\n\n*** Formatting data... ***"
        status_3 = "\n*** Writing data to csv-file... ***\n"
        status_4 = "*** Done ***"

        self.assertEqual(status_1, gefinder.status_report(1))
        self.assertEqual(status_2, gefinder.status_report(2))
        self.assertEqual(status_3, gefinder.status_report(3))
        self.assertEqual(status_4, gefinder.status_report(4))


    def test_remove_html_tags(self):

        html_string = "<li>Game - Store</li>"
        expected_result = "Game - Store"

        actual_result = gefinder.remove_html_tags(html_string)
        self.assertEqual(expected_result, actual_result)

    def test_reverse_string(self):

        test_string = "test"
        expected_result = "tset"

        actual_result = gefinder.reverse_string(test_string)
        self.assertEqual(expected_result, actual_result)

    def test_reverse_two_strings(self):

        test_string_1 = "one"
        test_string_2 = "two"
        expected_result_1 = "eno"
        expected_result_2 = "owt"

        actual_result_1, actual_result_2 = gefinder.reverse_two_strings(test_string_1, test_string_2)
        self.assertEqual(expected_result_1, actual_result_1)
        self.assertEqual(expected_result_2, actual_result_2)

    def test_strip_spaces(self):

        test_string_1 = " one "
        test_string_2 = " two "
        expected_result_1 = "one"
        expected_result_2 = "two"

        actual_result_1, actual_result_2 = gefinder.strip_spaces(test_string_1, test_string_2)
        self.assertEqual(expected_result_1, actual_result_1)
        self.assertEqual(expected_result_2, actual_result_2)


if __name__ == '__main__':
    unittest.main()
