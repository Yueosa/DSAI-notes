class SimpleSet:
    def __init__(self, initial_size=8):
        self.size = initial_size  # 初始桶数量
        self.buckets = [None] * self.size  # 初始化桶
        self.count = 0  # 元素计数
        self.load_factor = 0.7  # 负载因子阈值

    def _hash(self, element):
        """计算元素应存放的桶索引"""
        return hash(element) % self.size

    def _resize(self):
        """扩容并重新哈希所有元素"""
        old_buckets = self.buckets
        self.size *= 2  # 桶数量翻倍
        self.buckets = [None] * self.size
        self.count = 0

        for element in old_buckets:
            if element is not None:
                self.add(element)  # 重新插入元素

    def add(self, element):
        """添加元素到集合"""
        if self.count >= self.size * self.load_factor:
            self._resize()  # 触发扩容

        index = self._hash(element)
        
        # 开放寻址法解决冲突（线性探测）
        while self.buckets[index] is not None:
            if self.buckets[index] == element:
                return  # 元素已存在，直接返回
            index = (index + 1) % self.size  # 探测下一个位置

        self.buckets[index] = element
        self.count += 1

    def __contains__(self, element):
        """检查元素是否存在"""
        index = self._hash(element)
        while self.buckets[index] is not None:
            if self.buckets[index] == element:
                return True
            index = (index + 1) % self.size
        return False

    def __iter__(self):
        """实现遍历：按桶顺序返回非空元素"""
        for element in self.buckets:
            if element is not None:
                yield element

    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

"""
使用 print() 时会调用__str__
使用 x in s 时会调用__contains__
使用 for x in s 会调用__iter__, 返回迭代器
"""


if __name__ == '__main__':
    s = SimpleSet()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    print(s)

    print("__str__ 测试:", s)          # 调用 __str__
    print("__contains__ 测试:", 3 in s) # 调用 __contains__
    print("__iter__ 测试:", list(s))    # 调用 __iter__
