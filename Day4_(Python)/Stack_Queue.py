'''
🧩【今日练习题挑战】🧩
练习项目：小型任务管理器模拟器

🌟 要求：

有一个任务队列 (Queue) 管理新任务
    使用 collections 里的 deque (雙端隊列) 來模擬
    雙端隊列 支持 o(1) 時間複雜度從雙端添加、移除元素

有一个历史栈 (Stack) 记录已经完成的任务

可以添加任务、完成任务、查看下一个任务、查看历史记录
'''

from collections import deque


class SQ:
    """
    用於模擬 Stack、Queue 的結構
    """
    def __init__(self):
        """
        實例變量:
            self.stack: list: 用於保存已經完成的任務
            self.queue: deque: 用於管理等待中的任務
        """
        self.stack: list = []
        self.queue: deque = deque()


    def enqueue(self, task):
        """
        添加新任务到队列 self.queue
        append(): 
            語法爲 list.append(x), 返回 None, 是就地操作 (in-place)
        """
        self.queue.append(task)


    def dequeue(self):
        """
        完成当前任务：从队列出队，并加入历史栈
        queue.popleft(): 
            語法爲 queue.popleft(), 返回 隊首元素, 並從隊列中移除它
            如果 deque 爲空, 則會拋出 IndexError: pop from an empty deque
        """
        if not self.is_queue_empty():
            task = self.queue.popleft()
            self.stack.append(task)
            print(f"✅ 任务完成：{task}")
        else:
            print("🚫 没有任务可以完成。")


    def peek(self):
        """
        查看当前任务 (不移除)
        如果 queue 不爲空, 則返回第一個元素
        """
        return self.queue[0] if not self.is_queue_empty() else None


    def pop(self):
        """
        查看最近完成的任务 (历史)
        如果 stack 不爲空, 則返回最後一個元素
        """
        return self.stack[-1] if self.stack else None


    def history(self):
        """
        打印所有完成任务的记录
        如果 stack 不爲空, 則打印出所有完成的任務以及完成順序
        """
        if not self.stack:
            print("⚠️ 还没有任何完成的任务。")
        else:
            print("📜 完成记录：")
            for i, task in enumerate(self.stack):
                print(f"第 {i+1} 个完成的任务是：{task}")


    def is_queue_empty(self):
        """
        返回 queue 存儲信息
        如果 queue 爲空, 則返回 True
        """
        return len(self.queue) == 0
