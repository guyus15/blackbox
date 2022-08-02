## @file content_test.py
# @brief Contains tests to test the 'content' file and class.
# @author Guy Chamberlain-Webber

import unittest
import src.packet.content as content

this_content = None


## This test case tests the 'content' file and class.
class TestContent(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        global this_content

        this_content = content.Content(
            size=10,
            type=137,
            test_value=123
        )

    # Test 1
    def test_str(self):
        # This test ensures that the result of __str__ is as expected.
        global this_content

        expected_string = "Packet contents:\nsize: 10\ntype: 137\ntest_value: 123\n"

        self.assertEqual(this_content.__str__(), expected_string)

    # Test 2
    def test_check_exists_when_exists(self):
        # This test ensures that when a key exists in the content parameters,
        # the check_exists() method returns True.
        global this_content

        self.assertTrue(this_content.check_exists("size"))

    # Test 3
    def test_check_exists_no_exist(self):
        # This test ensures that when a key does not exist in the content parameters,
        # the check_exists() method returns False.
        global this_content

        self.assertFalse(this_content.check_exists("no existent parameter"))
