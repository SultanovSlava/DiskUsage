import unittest
from datetime import datetime
from unittest import mock
from inspect import getsourcefile
from os.path import abspath
from unittest.mock import patch

from catalog_filter import CatalogFilter
from command_line import CommandLine
from file_info import MyFile
from files_walking import FilesDetector
from outputing import Outputer


class TestMyFile(unittest.TestCase):
    def setUp(self):
        cur_file_name = abspath(getsourcefile(lambda: 0)).split('\\')[-1]
        self.test_dir_path = abspath(getsourcefile(lambda: 0))[:-len(cur_file_name)] + r'tests'
        self.file = MyFile(self.test_dir_path + r'\testFile.txt')

    def test_get_procent_zero_division_error(self):
        procent = self.file.get_procent(0)
        self.assertEqual(procent, 100)

    def test_get_procent(self):
        procent = self.file.get_procent(100)
        self.assertEqual(procent, self.file.size)

    def test_get_size(self):
        size = self.file.get_size(self.test_dir_path)
        self.assertEqual(size, self.file.size)

    def test_init(self):
        f = self.file
        self.assertEqual(f.name, 'testFile.txt')
        self.assertEqual(f.path, self.test_dir_path + r'\testFile.txt')
        self.assertEqual(f.nesting_level, 0)
        self.assertEqual(f.files_number, 0)
        self.assertEqual(f.extension, 'txt')


class TestFilesDetector(unittest.TestCase):

    def setUp(self):
        self.detector = FilesDetector()

    def test_walking(self):
        cur_file_name = abspath(getsourcefile(lambda: 0)).split('\\')[-1]
        test_dir_path = abspath(getsourcefile(lambda: 0))[:-len(cur_file_name)] + r'tests'
        file_name = test_dir_path + r'\testFile.txt'
        file = MyFile(file_name)
        self.detector.walking(test_dir_path)
        self.assertEqual(self.detector.total_size, 1)
        self.assertEqual(self.detector.level_files_and_dirs[test_dir_path][0].name, r'testFile.txt')

    def test_init(self):
        self.assertEqual(self.detector.cur_level, 0)
        self.assertEqual(self.detector.total_size, 0)
        self.assertEqual(self.detector.level_files_and_dirs, dict())


class TestOutputer(unittest.TestCase):

    def setUp(self):
        self.outputer = Outputer()

    def test_get_visual_procent(self):
        procent = 50
        visual = self.outputer.get_visual_procent(procent)
        self.assertEqual(visual, '[#####     ]')

    def test_output(self):
        cur_file_name = abspath(getsourcefile(lambda: 0)).split('\\')[-1]
        test_dir_path = abspath(getsourcefile(lambda: 0))[:-len(cur_file_name)] + r'tests'
        file_name = test_dir_path + r'\testFile.txt'
        file = MyFile(file_name)
        dir = [file]
        data = [
            ['Name', 'Procent', 'Size/FilesNum', 'Extension', 'Time'],
            ['testFile.txt', '[##########]', str(17) + 'B', 'txt',
             datetime.fromtimestamp(file.time)]
        ]
        self.assertEqual(self.outputer.output(dir), data)


class TestCatalogFilter(unittest.TestCase):
    def setUp(self):
        cur_file_name = abspath(getsourcefile(lambda: 0)).split('\\')[-1]
        test_dir_path = abspath(getsourcefile(lambda: 0))[:-len(cur_file_name)] + r'tests'
        file_name = test_dir_path + r'\testFile.txt'
        file = MyFile(file_name)
        self.test_catalog = [file]
        self.catalog_filter = CatalogFilter(self.test_catalog)

    def test_init(self):
        cf = CatalogFilter(self.test_catalog)
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_set_filter_by_author(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(author='John')
        self.assertEqual(len(cf.cur_catalog), 0)

    def test_set_filter_by_files_num(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(files_number='=0')
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_set_filter_by_files_num_more(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(files_number='+0')
        self.assertEqual(len(cf.cur_catalog), 0)

    def test_set_filter_by_files_num_less(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(files_number='-10')
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_set_filter_by_extension(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(extension='txt')
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_set_filter_by_size_more(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(size='+10')
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_set_filter_by_size(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(size='=17')
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_set_filter_by_size_less(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(size='-10')
        self.assertEqual(len(cf.cur_catalog), 0)

    def test_set_filter_by_level(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(level='=0')
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_set_filter_by_level_more(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(level='+0')
        self.assertEqual(len(cf.cur_catalog), 0)

    def test_set_filter_by_level_less(self):
        cf = CatalogFilter(self.test_catalog)
        cf.set_filter(level='-5')
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_reset_filter(self):
        cf = CatalogFilter(self.test_catalog)
        cf.reset_filter()
        self.assertEqual(len(cf.cur_catalog), 1)

    def test_group_by(self):
        cf = CatalogFilter(self.test_catalog)
        cf.group_by('extension')
        self.assertEqual(len(cf.cur_catalog), 1)


class TestCommandLine(unittest.TestCase):
    def setUp(self):
        self.cl = CommandLine()
        cur_file_name = abspath(getsourcefile(lambda: 0)).split('\\')[-1]
        self.test_dir_path = abspath(getsourcefile(lambda: 0))[:-len(cur_file_name)] + r'tests'

    def test_command_processing_stop(self):
        result = self.cl.command_processing('stop')
        self.assertEqual(result, 'stop')

    def test_command_processing_w(self):
        self.cl.files_detector.walking = mock.MagicMock()
        self.cl.command_processing('w some_dir')
        self.cl.files_detector.walking.assert_called_with('some_dir')

    def test_command_processing_d(self):
        self.cl.files_detector.level_files_and_dirs = {'dir1': 'file1', 'dir2': 'file2'}
        self.cl.catalog_filter = mock.MagicMock()
        self.cl.outputer.output = mock.MagicMock()
        self.cl.command_processing('d dir1')
        self.assertEqual(self.cl.catalog_filter.call_count, 0)

    def test_command_processing_f_reset(self):
        self.cl.catalog_filter.reset_filter = mock.MagicMock()
        self.cl.command_processing('f reset')
        self.cl.catalog_filter.reset_filter.assert_called_once()

    def test_command_processing_f_with_filter(self):
        self.cl.catalog_filter.set_filter = mock.MagicMock()
        self.cl.outputer.output = mock.MagicMock()
        self.cl.command_processing('f extension:txt')
        self.cl.catalog_filter.set_filter.assert_called_with(extension='txt')
        self.assertEqual(self.cl.outputer.output.call_count, 1)

    def test_command_processing_g(self):
        self.cl.catalog_filter.group_by = mock.MagicMock()
        self.cl.outputer.output = mock.MagicMock()
        self.cl.command_processing('g extension')
        self.cl.catalog_filter.group_by.assert_called_with('extension')
        self.assertEqual(self.cl.outputer.output.call_count, 1)


if __name__ == '__main__':
    unittest.main()
