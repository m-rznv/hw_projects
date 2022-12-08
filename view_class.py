from abc import ABC, abstractmethod
from datetime import datetime as dt


class View(ABC):
    @abstractmethod
    def show_content(self):
        pass


class CommandsView(View):

    def __init__(self, command_list, align, spaces):
        self.commands = command_list
        self.align = align
        self.spaces = spaces

    def show_content(self):
        format_str = str('{:%s%d}' % (self.align, self.spaces))
        for command in self.commands:
            print(format_str.format(command))


class BookView(View):
    def __init__(self, account, align='<', spaces=0):
        self.align = align
        self.spaces = spaces
        self.account = account

    def show_content(self):
        if self.account['birthday']:
            birth = self.account['birthday'].strftime("%d/%m/%Y")
        result = "_" * self.spaces + "\n" + \
            f"Name: {self.account['name']} \nPhones: {', '.join(self.account['phones'])} \nBirthday: {birth} \nEmail: {self.account['email']} \nStatus: {self.account['status']} \nNote: {self.account['note']}\n" + "_" * self.spaces
        print(result)


class Logs:

    def __init__(self):
        pass

    def log(self, action):
        current_time = dt.strftime(dt.now(), '%H:%M:%S')
        message = f'[{current_time}] {action}'
        with open('logs.txt', 'a') as file:
            file.write(f'{message}\n')
