class Tool:
    def Toolpush(self, list: list, index: int, item, priority):
        itemset = (priority, index, item)
        list.append(itemset)
        return self._bubble_up(list, len(list) - 1)
    
    def _bubble_up(self, list: list, index: int):
        while index > 0:
            parent_idx = (index - 1) // 2
            if list[index][0] < list[parent_idx][0]:
                list[index], list[parent_idx] = list[parent_idx], list[index]
                index = parent_idx
            else:
                break
        return list


class Weiba:
    def __init__(self):
        self.list = []
        self.index = 0
        self.tool = Tool()

    def push(self, item, priority):
        self.list = self.tool.Toolpush(self.list, self.index, item, priority)
        self.index += 1
        return None
    
    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[0]

    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

