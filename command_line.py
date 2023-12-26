from outputing import Outputer
from catalog_filter import CatalogFilter
from files_walking import FilesDetector


class CommandLine:
    def __init__(self):
        self.files_detector = FilesDetector()
        self.catalog_filter = CatalogFilter()
        self.directory = []
        self.outputer = Outputer()

    def run(self):
        print('Input command:')

        while True:
            command = input()
            if self.command_processing(command) == 'stop':
                break

    def command_processing(self, command):
        try:
            if command == 'stop':
                print('Stop command line')
                return 'stop'
            commands = command.split()
            command_type = commands[0]
            message = commands[1]
            if command_type == 'w':
                try:
                    self.files_detector.walking(message)
                    self.directory = self.files_detector.level_files_and_dirs[message]
                    print('w Ok')
                except FileNotFoundError as e:
                    print(e)
            elif command_type == 'd':
                try:
                    self.directory = self.files_detector.level_files_and_dirs[message]
                    self.catalog_filter = CatalogFilter(self.directory)
                    self.outputer.output(self.directory)
                    print('d Ok')
                except KeyError as e:
                    print('uncorrect directory path')
            elif command_type == 'f':
                if message == 'reset':
                    self.catalog_filter.reset_filter()
                    print('reset Done')
                elif len(message) != 0:
                    key, value = message.split(':')
                    self.outputer.output(self.catalog_filter.set_filter(**{key: value}).values())
                else:
                    print('Unknown filter message type')
            elif command_type == 'g':
                self.outputer.output(self.catalog_filter.group_by(message))
            else:
                print('Unknown command')
        except Exception:
            print('Incorrect command')
