'''
🧩【今日练习题挑战】🧩
练习项目：小型任务管理器模拟器

🌟 要求：

有一个任务队列(Queue)管理新任务

有一个历史栈(Stack)记录已经完成的任务

可以添加任务、完成任务、查看下一个任务、查看历史记录
'''

from collections import deque

class SQ:
    def __init__(self):
        self.stack = []          # 用于保存完成的任务记录（历史）
        self.queue = deque()     # 用于管理等待中的任务

    def enqueue(self, task):
        """添加新任务到队列"""
        self.queue.append(task)

    def dequeue(self):
        """完成当前任务：从队列出队，并加入历史栈"""
        if not self.is_queue_empty():
            task = self.queue.popleft()
            self.stack.append(task)
            print(f"✅ 任务完成：{task}")
        else:
            print("🚫 没有任务可以完成。")

    def peek(self):
        """查看当前任务（不移除）"""
        return self.queue[0] if not self.is_queue_empty() else None

    def pop(self):
        """查看最近完成的任务（历史）"""
        return self.stack[-1] if self.stack else None

    def history(self):
        """打印所有完成任务的记录"""
        if not self.stack:
            print("⚠️ 还没有任何完成的任务。")
        else:
            print("📜 完成记录：")
            for i, task in enumerate(self.stack):
                print(f"第 {i+1} 个完成的任务是：{task}")

    def is_queue_empty(self):
        return len(self.queue) == 0
