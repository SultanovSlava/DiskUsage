from pprint import pp

import pandas
from pandas import DataFrame
import itertools as it
import operator as op


class filter:
    def __init__(self, catalog):
        dict_of_catalog = dict()
        for el in catalog:
            dict_of_catalog[el.path] = el
        self.cur_catalog = dict_of_catalog
        self.catalog = dict_of_catalog
        self.author_filter = None
        self.extension_filter = None
        self.date_filter = None
        self.size_filter = None
        self.level_filter = None
        self.files_number_filter = None

    def set_filter(self, author=None, extension=None, date=None, size=None, level=None, files_number=None):
        if level is not None:
            self.level_filter = level
            self.filt_by_level()
        if date is not None:
            self.date_filter = date
            self.filt_by_date()
        if files_number is not None:
            self.files_number = files_number
            self.filt_by_files_number()
        if author is not None:
            self.author_filter = author
            self.filt_by_author()
        if extension is not None:
            self.extension_filter = extension
            self.filt_by_extension()
        if size is not None:
            self.size_filter = size
            self.filt_by_size()

        return self.cur_catalog

    def reset_filter(self):
        self.author_filter = False
        self.extension_filter = False
        self.date_filter = False
        self.size_filter = False
        self.level_filter = False
        self.cur_catalog = self.catalog

    def filt_by_extension(self):
        filt_result = dict()
        for el in self.cur_catalog:
            for extension in self.extension_filter:
                if self.cur_catalog[el].extension == extension:
                    filt_result[el] = self.cur_catalog[el]
        self.cur_catalog = filt_result

    def filt_by_files_number(self):
        filt_result = dict()
        for el in self.cur_catalog:
            if self.cur_catalog[el].files_number == self.files_number:
                filt_result[el] = self.cur_catalog[el]
        self.cur_catalog = filt_result

    def filt_by_author(self):
        filt_result = dict()
        for el in self.cur_catalog:
            for author in self.author_filter:
                if self.cur_catalog[el].author == author:
                    filt_result[el] = self.cur_catalog[el]
        self.cur_catalog = filt_result

    def filt_by_date(self):
        filt_result = dict()
        filt_type = self.date_filter[0]

        for path in self.cur_catalog:
            el = self.cur_catalog[path]
            if filt_type == '+' and el.time >= int(self.date_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '-' and el.time < int(self.date_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '=' and el.time == int(self.date_filter[1:]):
                filt_result[el.path] = el

        self.cur_catalog = filt_result

    def filt_by_size(self):
        filt_result = dict()
        filt_type = self.size_filter[0]

        for path in self.cur_catalog:
            el = self.cur_catalog[path]
            if filt_type == '+' and el.size >= int(self.size_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '-' and el.size < int(self.size_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '=' and el.size == int(self.size_filter[1:]):
                filt_result[el.path] = el

        self.cur_catalog = filt_result

    def filt_by_level(self):
        filt_result = dict()
        filt_type = self.level_filter[0]

        for path in self.cur_catalog:
            el = self.cur_catalog[path]
            if filt_type == '+' and el.level >= int(self.level_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '-' and el.level < int(self.level_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '=' and el.level == int(self.level_filter[1:]):
                filt_result[el.path] = el

        self.cur_catalog = filt_result

    def group_by(self, group_key):
        catalog_sort_by_key = dict()
        for el in self.cur_catalog.values():
            catalog_sort_by_key[el] = getattr(el, group_key)
        catalog_sort_by_key = sorted(catalog_sort_by_key.items(), key=lambda item: item[1])
        group_catalog = dict(catalog_sort_by_key)
        # print(group_catalog.values())
        return group_catalog.keys()
        # df_catalog = DataFrame(self.cur_catalog.values(), index=[])
        # print(df_catalog.keys())
        # return df_catalog.groupby(group_key)
