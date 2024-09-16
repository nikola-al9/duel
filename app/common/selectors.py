from abc import ABC, abstractmethod

class SelectorAbstract(ABC):

    def __init__(self, user, *args, **kwargs):
        self.reset()
        self.user = user

    def reset(self):
        self.user = None