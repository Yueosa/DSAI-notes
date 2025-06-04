# AIManager 雏形 - 管理继承体系与实例
from typing import List, Dict, Type


class AI(object, metaclass=type):
    """
    所有AI类的基类
    """
    def __init__(self, name: str) -> None:
        """
        作用: 自动注册 AI, 通过触发 AIManager 的 regsiter_instance 方法

        参数:
            self(obj): 实例本身
            name(str): AI的名字
        """
        self.name: str = name
        AIManager.register_instance(self)

    def say(self) -> None:
        """guess number
        作用: 输出当前 AI 的信息, 以及他的来源
        """
        print(f"我是 {self.name}, 来自 {self.__class__.__name__}")


class AIManager(object, metaclass=type):
    """
    管理器类

    初始化类变量:
        regsitered_classes: 存储 “子类名: str -> 父类名: Dict[str, tuple[str, ...]]” 的映射
        instance: 存储所有 AI 实例信息
    """
    registered_classes: Dict[str, tuple[str, ...]] = {}
    instances: List[Dict[str, str]] = []


    @classmethod
    def register_class(cls, child_class: Type[AI]) -> None:
        """
        作用: 获取类的直接父类信息, 并且存进字典

        参数:
            cls: 管理类本身
            child_class: 需要注册的类
        
        操作:
            检查子类名是否存在于字典中(使用 .__name__ 获取子类名)
            如果不存在: 
                获取子类的直接父类信息(使用 .__bases__ 得到 (<class '__main__.type'>,))
                将 “子类名: str -> 父类名: Dict[str, tuple[str, ...]]” 存进字典中
        """
        name: str = child_class.__name__
        if name not in cls.registered_classes:
            bases: tuple[Type, ...] = child_class.__bases__
            cls.registered_classes[name] = tuple(base.__name__ for base in bases)


    @classmethod
    def register_instance(cls, obj: Type[AI]):
        """
        作用: 将父子集信息加入 instance 列表

        参数: 
            cls: 管理类本身
            obj: 需要添加的实例对象
        
        操作:
            将 {"name": str, "class": str} 存储到 instance 中
        """
        cls.instances.append({
            "name": obj.name,
            "class": obj.__class__.__name__
        })


    @classmethod
    def show_instances(cls):
        """
        作用: 输出 instance 里的所有信息
        """
        print("\n📦 当前 AI 实例：")
        for i in cls.instances:
            print(f"- {i['name']} ({i['class']})")


    @classmethod
    def show_class_tree(cls):
        """
        作用: 输出 regsistered_classes 里的所有信息
        """
        print("\n🌳 类继承树：")
        for child, parent in cls.registered_classes.items():
            print(f"- {child} ← {parent}")


    @staticmethod
    def auto_register(reg_cls: Type[AI]):
        """
        作用: 自动注册机, 将继承树进 registered_classes

        参数:
            cls: 需要注册的类
        返回:
            cls: 注册完成的类本身
        """
        AIManager.register_class(reg_cls)
        return reg_cls


@AIManager.auto_register
class BattleAI(AI, metaclass=type):
    """
    基于 AI 继承一个 BattleAI
    """
    pass


@AIManager.auto_register
class PetAI(AI, metaclass= type):
    """
    基于 AI 继承一个 PetAI, 并且重写 say 方法
    """
    def say(self):
        print(f"{self.name}：喵呜喵呜～")


if __name__ == '__main__':
    Zbot: BattleAI = BattleAI("Zero") # 实例化 BattleAI, name 参数为 Zero
    Cbot: PetAI = PetAI("Catbot") # 实例化 PetAI, name 参数为 Catbot

    Zbot.say() # 调用 Zbot 的 say 方法, 这是从 AI 类中继承的方法
    Cbot.say() # 调用 Cbot 的 say 方法, 这是在 PetAI 类中重写过的方法

    AIManager.show_instances() # 输出 instance 信息
    AIManager.show_class_tree() # 输出 registered_classes 信息
