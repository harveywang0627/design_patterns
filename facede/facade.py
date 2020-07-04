from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum()


class Server(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.__doc__

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):

    def __init__(self):
        """ container """
        self.name = 'FileServer'
        self.state = State.new
        super().__init__()

    def boot(self):
        print('booting the {}'.format(self))
        '''start'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''kill operation'''
        self.state = State.restart if restart else State.zombie

    @staticmethod
    def create_file(user, name, permissions):
        """check permission"""
        print("trying to create the file '{}' for user '{}' with permissions {}".format(name, user, permissions))


class ProcessServer(Server):
    def __init__(self):
        """initialize"""
        self.name = 'ProcessServer'
        self.state = State.new
        super().__init__()

    def boot(self):
        print('booting the {}'.format(self))
        '''start'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''Kill all'''
        self.state = State.restart if restart else State.zombie

    @staticmethod
    def create_process(user, name):
        """check user process"""
        print("trying to create the process '{}' for user '{}'".format(name, user))


class OperatingSystem:
    """facade"""
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)
