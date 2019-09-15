import unittest
import read_files
import write_files

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

    def file_write_helper(filepath, contents):
        with open(filepath, 'w') as f:
            f.write(contents)

    def file_read_helper(filepath, as_lines):
        with open(filepath, 'r') as f:
            lines = f.readlines()
            if as_lines:
                return lines
            else:
                return "".join(lines)

    def test_foo_function(self):
        pass

if __name__ == '__main__':
    unittest.main()
