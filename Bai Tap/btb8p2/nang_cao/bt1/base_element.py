# Bài nâng cao 1: Xây dựng hệ thống Element
from abc import ABC, abstractmethod


class BaseElement(ABC):
    def __init__(self, locator):
        self.__locator = locator   # private: lớp con cũng không truy cập trực tiếp được

    def get_locator(self):
        # Phương thức public để lấy locator từ bên ngoài
        return self.__locator

    @abstractmethod
    def click(self):
        pass
