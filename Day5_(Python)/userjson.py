import json

class JsonHandler:
    def __init__(self, filename='user_info.json'):
        self.filename = filename
        self.index = 0

    def json_dump(self, data):
        """写入 JSON 数据"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return data

    def json_load(self):
        """读取 JSON 数据"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("文件不存在")
            return None

    def get_user_input(self):
        """获取用户输入"""
        name = input("请输入姓名: ")
        age = input("请输入年龄: ")
        interest = input("请输入兴趣: ")
        return {'name': name, 'age': age, 'interest': interest}

    def operate(self):
        """操作生成器"""
        while True:
            self.index = (self.index + 1) % 2
            if self.index == 1:
                # 写入模式
                user_data = self.get_user_input()
                result = self.json_dump(user_data)
                yield ("写入", result)
            else:
                # 读取模式
                result = self.json_load()
                yield ("读取", result)
