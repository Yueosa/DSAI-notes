
# `heapq.heappush` 方法源码总结

`heapq` 模块中的 `heappush` 方法用于将新元素添加到堆中，并保持堆的性质。下面是该方法的解释、算法及其输出结果的总结。

### 函数定义
```python
def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
```

### 输入
- **`heap`** (列表): 表示堆的列表。堆在调用 `heappush` 之前必须是一个有效的堆。
- **`item`** (任何类型): 需要添加到堆中的新元素。该元素会根据堆的性质被放置在正确的位置。

### 处理过程（算法）
1. **追加元素**: 通过 `heap.append(item)` 将 `item` 追加到 `heap` 列表的末尾。这个操作将元素暂时放置在堆的最后一个位置。
2. **调整堆**: 调用 `_siftdown` 方法，将 `item` 移动到堆中的正确位置。该过程通过比较元素与其父元素的值，保持堆的性质，即父元素总是小于或等于其子元素。

`_siftdown` 方法的定义如下:
```python
def _siftdown(heap, startpos, pos):
    newitem = heap[pos] # 保存待调整元素
    while pos > startpos:
        parentpos = (pos - 1) >> 1 # 计算父节点位置(等价于(pes - 1) // 2)
        parent = heap[parentpos]
        if newitem < parent: # 最小堆: 子节点 < 父节点时需要替换
            heap[pos] = parent # 父节点下移
            pos = parentpos # 向上检查
            continue
        break # 以满足堆属性时终止
    heap[pos] = newitem # 最终定位新元素
```
在 `_siftdown` 函数中:
- 元素与其父元素的值进行比较。
- 如果 `item` 小于父元素，它们交换位置，并继续与新的父元素进行比较。
- 这个过程会一直进行，直到元素到达正确的位置，不再需要与父元素交换位置。

### 输出
- **修改后的 `heap`**: 执行 `heappush` 方法后，输入的堆会被原地修改，新的元素会被插入到堆中的正确位置。
- 堆会保持有效的最小堆性质，即父元素总是小于或等于其子元素。

### 示例
```python
import heapq

heap = [1, 3, 5, 7, 9, 2]
heapq.heappush(heap, 4)
print(heap)  # 输出将会是: [1, 3, 2, 7, 9, 5, 4]
```

### 总结
`heappush` 方法通过将新元素追加到堆末尾，并将其“向下调整”到正确位置，来有效地保持堆的性质。该算法的时间复杂度为 `O(log n)`，其中 `n` 是堆中的元素数量。
