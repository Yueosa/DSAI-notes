# AIManager 雏形 - 管理继承体系与实例

class AI:
    def __init__(self, name):
        self.name = name
        AIManager.register_instance(self)

    def say(self):
        print(f"我是 {self.name}, 来自 {self.__class__.__name__}")


class AIManager:
    registered_classes = {}  # 子类名 -> 父类名
    instances = []           # 所有 AI 实例

    @classmethod
    def register_class(cls, child_class):
        if child_class.__name__ not in cls.registered_classes:
            bases = child_class.__bases__
            if bases:
                cls.registered_classes[child_class.__name__] = bases[0].__name__

    @classmethod
    def register_instance(cls, obj):
        cls.instances.append({
            "name": obj.name,
            "class": obj.__class__.__name__
        })

    @classmethod
    def show_instances(cls):
        print("\n📦 当前 AI 实例：")
        for i in cls.instances:
            print(f"- {i['name']} ({i['class']})")

    @classmethod
    def show_class_tree(cls):
        print("\n🌳 类继承树：")
        for child, parent in cls.registered_classes.items():
            print(f"- {child} ← {parent}")


# 示例子类
def auto_register(cls):
    AIManager.register_class(cls)
    return cls


@auto_register
class BattleAI(AI):
    pass

@auto_register
class PetAI(AI):
    def say(self):
        print(f"{self.name}：喵呜喵呜～")


# 使用示例
bot1 = BattleAI("Zero")
bot2 = PetAI("Catbot")

bot1.say()
bot2.say()

AIManager.show_instances()
AIManager.show_class_tree()
