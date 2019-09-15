import unittest
import read_files
import write_files
import io
import sys

class Problem4Test(unittest.TestCase):
    valid_json_string = """
    {
        "something": "foo",
        "otherThing": 2
    }
    """

    invalid_json_string = """
    {
        "something": "foo,
        {{{{

        }}
    }
    """

    def setUp():
        self.old_output = sys.stdout
        self.output_capture = io.StringIO()
        sys.stdout = self.output_capture

    def tearDown():
        self.output_capture.close()
        syst.stdout = self.old_output

    def _file_write_helper(filepath, contents):
        with open(filepath, 'w') as f:
            f.write(contents)

    def _file_read_helper(filepath, as_lines):
        with open(filepath, 'r') as f:
            lines = f.readlines()
            if as_lines:
                return lines
            else:
                return "".join(lines)

    def test_read_file(self):
        path = "./test_files/read1.txt"
        read_files.read_file(path)
        self.assertEqual("abc123", self.output_capture.getvalue())

if __name__ == '__main__':
    unittest.main()
