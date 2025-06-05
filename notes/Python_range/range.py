from typing import Iterable


def thedir() -> None:
    def foo(): pass

    A: type = type("A", (object,), {"foo": foo})
    print(dir(A))


class MyRange(object, metaclass=type):
    def __init__(self, start: int, end: int, step: int = 1):
        self.start: int = start
        self.stop: int = end
        self.step: int = step

    def __iter__(self):
        return MyRangeIterator(self.start, self.stop, self.step)


class MyRangeIterator(object, metaclass=type):
    def __init__(self, start: int, stop: int, step: int):
        self.current: int = start
        self.stop: int = stop
        self.step: int = step


    def __next__(self) -> int:
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.start <= self.stop):
            raise StopIteration
        
        value: int = self.current
        self.current += self.step
        return value


if __name__ == '__main__':
    thedir()
    r = MyRange(0, 10, 2)
    for i in r:
        print(i)
