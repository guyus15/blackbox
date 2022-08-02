## @file content_test.py
# @brief Contains tests to test the 'content' file and class.
# @author Guy Chamberlain-Webber

import unittest
import src.packet.content as content

this_content = None


## This test case tests the 'content' file and class.
class TestContent(unittest.TestCase):
    def setUp(self) -> None:
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

    # Test 4
    def test_get_byte_array(self):
        # This test ensures that when the get_byte_array() method is called, it returns the expected result,
        # a byte of array representing the content parameter values.
        global this_content

        expected_result = [b'\x0a', b'\x89', b'\x7b']

        self.assertEqual(this_content.get_byte_array(), expected_result)

    # Test 5
    def test_get_byte_array_w_string(self):
        # This test ensures that when the get_byte_array() method is called when strings are present in the
        # content parameters, the expected result is still returned.

        new_content = content.Content(some_string="string1")

        expected_result = [b"\x73", b"\x74", b"\x72", b"\x69", b"\x6e", b"\x67", b"\x31"]

        self.assertEqual(new_content.get_byte_array(), expected_result)

    # Test 6
    def test_set_parameter_valid_key(self):
        # This test ensures that when the set_parameter() method is called with an existing key,
        # the value corresponding to that key is set correctly.
        global this_content

        # Change the value of the 'size' parameter.
        this_content.set_parameter("size", 20)

        self.assertEqual(this_content._params["size"], 20)

    # Test 7
    def test_set_parameter_invalid_key(self):
        # This test ensures that when the set_parameter() method is called with a non-existent key,
        # an AttributeError is raised.
        global this_content

        with self.assertRaises(AttributeError) as cm:
            this_content.set_parameter("non-existent parameter", "some value")

        exception = cm.exception
        self.assertIsNotNone(exception)
