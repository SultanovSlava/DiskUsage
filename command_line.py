import output
from catalog_filter import catalog_filter
from files_walking import files_detector


class command_line:
    def __init__(self):
        self.files_detector = files_detector()
        self.catalog_filter = catalog_filter()
        self.directory = []
        self.run()

    def run(self):
        print('Input command:')

        while True:
            command = input()
            if command == 'stop':
                print('Stop')
                break
            commands = command.split()
            command_type = commands[0]
            message = commands[1]
            if command_type == 'w':
                self.files_detector.walking(message)
                self.directory = self.files_detector.level_files_and_dirs[message]
                print('w Ok')
            elif command_type == 'd':
                self.directory = self.files_detector.level_files_and_dirs[message]
                self.catalog_filter = catalog_filter(self.directory)
                print('d Ok')
            elif command_type == 'f':
                if message == 'reset':
                    self.catalog_filter.reset_filter()
                    print('reset Done')
                else:
                    key, value = message.split(':')
                    output.output(self.catalog_filter.set_filter(**{key: value}).values())
            elif command_type == 'g':
                output.output(self.catalog_filter.group_by(message))
