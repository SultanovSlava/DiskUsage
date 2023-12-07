import file_info
import queue


class filter:
    def __init__(self, catalog):
        self.cur_catalog = catalog
        self.catalog = catalog
        self.author_filter = False
        self.extension_filter = False
        self.date_filter = False
        self.size_filter = False
        self.level_filter = False

    def set_filter(self, author=None, extension=None, date=None, size=None, level=None):
        if level is not None:
            self.level_filter = level
            # self.filt_by_level()
        if date is not None:
            self.date_filter = date
            self.filt_by_date()
        if author is not None:
            self.author_filter = author
            self.filt_by_author()
        if extension is not None:
            self.extension_filter = extension
            self.filt_by_extension()
        if size is not None:
            self.size_filter = size

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

        for el in self.cur_catalog:
            if filt_type == '+' and el.time >= int(self.date_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '-' and el.time < int(self.date_filter[1:]):
                filt_result[el.path] = el
            elif filt_type == '=' and el.time == int(self.date_filter[1:]):
                filt_result[el.path] = el

        self.cur_catalog = filt_result

    # def filt_by_level(self):
    #   filt_result = dict()
    #  catalogs_by_levels = queue.Queue(self.cur_catalog)
    #
    # while catalogs_by_levels
    #       .level != self.level_filter - 1:
    #      filt_result[el] = self.catalog[el]
    # self.cur_catalog = filt_result
