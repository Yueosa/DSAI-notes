
# Python `range()` 对象深度解析

## ✅ `range()` 是什么对象？

在 Python 中，`range()` 返回的是一个 **range 对象**，它是一个 **不可变的序列类型**，其底层实现为一个轻量级的对象，不会直接生成完整的序列数据，而是 **按需计算** 元素。这与 `list` 或 `tuple` 明显不同，后两者会将所有元素存储在内存中。

```python
print(type(range(10)))   # <class 'range'>
```

---

## ✅ `range()` 与 `list` 的区别

- **`list()`：** 会直接将整个序列存储在内存中，占用内存较多。

```python
lst = list(range(10))
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

- **`range()`：** 并不会立即生成具体数据，而是按需计算，在需要访问某个索引时才生成对应值，这种 **惰性计算** 的方式节省了内存。

```python
r = range(10)
print(r)        # range(0, 10)
print(r[3])     # 3
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## ✅ `range()` 与迭代器 (Iterator) 的区别

`range()` 是一个 **可迭代对象 (Iterable)**，但它 **不是迭代器 (Iterator)**。

```python
r = range(10)
print('__iter__' in dir(r))    # True
print('__next__' in dir(r))    # False

iter_r = iter(r)
print(next(iter_r))  # 0
print(next(iter_r))  # 1
```

---

## ✅ `range()` 的底层实现

### **`rangeobject.c`：**

```c
typedef struct {
    PyObject_HEAD
    PyObject *start;
    PyObject *stop;
    PyObject *step;
    Py_ssize_t length;
} rangeobject;
```

### `rangeitem()` 方法：

```c
static PyObject *
rangeitem(rangeobject *r, Py_ssize_t index)
{
    if (index < 0 || index >= r->length) {
        PyErr_SetString(PyExc_IndexError, "range object index out of range");
        return NULL;
    }

    return PyLong_FromSsize_t(PyLong_AsSsize_t(r->start) + index * PyLong_AsSsize_t(r->step));
}
```

---

## ✅ 内存优化与时间复杂度

- **内存占用：** `range()` 只保存 `start`, `stop`, `step` 和 `length`，而不是整个序列。
- **时间复杂度：** `O(1)`，直接计算索引值。
- **空间复杂度：** `O(1)`，仅保存固定属性。

---

## ✅ 模拟 `range()` 的惰性序列

```python
class MyRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return MyRangeIterator(self.start, self.stop, self.step)

class MyRangeIterator:
    def __init__(self, start, stop, step):
        self.current = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for i in MyRange(0, 10, 2):
    print(i)
```

---

## ✅ 总结

- `range()` 是 **轻量级惰性序列对象**，按需计算，不存储完整序列，仅保存起始、终止和步长信息。
- `range()` 是 **不可变序列对象**，不像 `list` 会一次性加载所有元素。
- `range()` 可以被 `iter()` 转换为迭代器，但本身不是迭代器。
- 底层 C 实现中，`range` 的核心是利用简单的加法运算计算每个元素，从而实现 `O(1)` 的时间复杂度和 `O(1)` 的空间复杂度。
