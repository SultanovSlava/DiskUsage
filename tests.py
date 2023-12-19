import os
import sys
import unittest
from unittest import mock



from file_info import MyFile


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


class TestMyFileMethods(unittest.TestCase):
    def setUp(self):
        #with open("testfile.txt", "w") as file:
         #   file.write("This is a test file for testing purposes")
        self.file = MyFile('.')

    def test_get_procent(self):
        self.assertEqual(self.file.get_procent(1000), 0)
        self.assertEqual(self.file.get_procent(0), 100)


    def test_init(self):
        self.file = MyFile("testfile.txt")
        self.assertEqual(self.file.name, "testfile.txt")
        self.assertEqual(self.file.extension, "txt")
        self.assertIsNotNone(self.file.time)
        self.assertIsNotNone(self.file.author)
        self.assertEqual(self.file.nesting_level, 0)
        self.assertEqual(self.file.files_number, 0)
        self.assertEqual(self.file.size, 0)

    def tearDown(self):
        os.unlink("testfile.txt")


if __name__ == '__main__':
    unittest.main()

