from numbers import Complex
from collections.abc import MutableSequence
from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self):
        pass
class Number(Complex):
    pass

class Playlist(MutableSequence):
    pass

# It will throw an error
# TypeError: Can't instantiate abstract class Playlist with abstract methods __delitem__, __getitem__, __len__, __setitem__, insert
playlist = Playlist()