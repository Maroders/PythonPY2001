import json

from typing import Iterable
from abc import ABC, abstractmethod



class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


class JsonFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> list:
        """
        Считывает и записывает данные в (например LinkedList)
        :param data:
        :return:
        """

        with open(self.filename, "r") as f:
            json_data = json.load(f)
            return json_data



    def write(self, data: list) -> None:

        """
        Считывает из (например LinkedList) и записывает в файл
        :param data:
        :return:
        """

        if not isinstance(data, list):
            raise TypeError("Not list sent")

        with open(self.filename, "w") as f:
            json.dump(data, f)
# TODO Реализовать класс JsonFileDriver


if __name__ == "__main__":
    jsndrv = JsonFileDriver("somefilename.json")

    jsndrv.write([1, 2, 3])

    for_print = jsndrv.read()
    print(for_print)


