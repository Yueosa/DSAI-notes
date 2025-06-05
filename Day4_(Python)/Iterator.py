from typing import Iterator


class Counter(object, metaclass=type):
    """
    模拟迭代器原理

    方法:
        __iter__: 返回实例本身, 是一个迭代器对象
        __next__: 逐步输出对象
    """
    def __init__(self, start: int, end: int):
        self.left_num: int = start
        self.right_num: int = end

    def __iter__(self) -> Iterator[int]:
        return self

    def __next__(self) -> int:
        if self.left_num > self.right_num:
            raise StopIteration
        self.left_num += 1
        return self.left_num - 1


if __name__ == '__main__':
    counter: Iterator[int] = Counter(1, 3)
    print(next(counter))
    print(next(counter))
