from abc import ABC, abstractmethod


class Steganograph(ABC):
    @abstractmethod
    def __init__(self):
        ...