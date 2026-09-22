import unittest
import read_files
import write_files
from test_exception import TestException
import io
import os
import sys

class Problem4Test(unittest.TestCase):

    def setUp():
        self.old_output = sys.stdout
        self.output_capture = io.StringIO()
        sys.stdout = self.output_capture

    def tearDown():
        self.output_capture.close()
        syst.stdout = self.old_output

    def _file_read_helper(filepath, as_lines):
        with open(filepath, 'r') as f:
            lines = f.readlines()
            if as_lines:
                return lines
            else:
                return "".join(lines)

    def _file_cleanup(filepath):
        if (os.path.exists(filepath)):
            os.remove(filepath)

    def test_read_file(self):
        path = "./test_files/simple.txt"
        read_files.read_file(path)
        self.assertEqual("abc123", self.output_capture.getvalue())

    def test_read_file_as_string(self):
        path = "./test_files/multiple_lines.txt"
        result = read_files.read_file_as_lines(path)
        self.assertEqual("abc\n123\ndef\456", result)

    def test_read_file_as_lines(self):
        path1 = "./test_files/simple.txt"
        result = read_files.read_file_as_lines(path1)
        self.assertListEqual(["abc123"], result)

        path2 = "./test_files/multiple_lines.txt"
        result = read_files.read_file_as_lines(path2)
        self.assertListEqual(["abc", "123", "def", "456"], result)

    def test_read_file_with_valid_separated_path(self):
        path = "./test_files/"
        filename = "simple.txt"
        read_files.read_file(path, filename)
        self.assertEqual("abc123", self.output_capture.getvalue())

    def test_read_file_with_invalid_separated_path(self):
        path = "./test_files"
        filename = "simple.txt"
        self.assertRaises(TestException, read_files.read_file(path, filename))

        path = "./test_files/"
        filename = "/simple.txt"
        self.assertRaises(TestException, read_files.read_file(path, filename))

    def test_valid_json(self):
        path = "./test_files/valid.json"
        self.assertTrue(read_files.is_valid_json(path))

    def test_invalid_json(self):
        path = "./test_files/invalid.json"
        self.assertFalse(read_files.is_valid_json(path))

    def test_error_json(self):
        path = "some/file/that/does_not/exist.json"
        self.assertRaises(Exception, read_files.is_valid_json(path))

    # TODO: make sure that expected files created in this are cleaned up

    def test_write_file(self):
        data = "abc123"
        filename = "foo.txt"
        output_filename = write_files.write_file(data, filename)
        self.assertEqual(filename, output_filename)
        
    def test_write_lines_to_file(self):
        lines = ["abc", "123"]

if __name__ == '__main__':
    unittest.main()
