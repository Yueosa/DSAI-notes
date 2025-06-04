"练习: 猜数字小游戏"

import random

def parse_range_input(prompt: str) -> int:
    """获取用户输入并转换为整数，自动去除空格"""
    while True:
        raw: str = input(prompt).strip()
        if raw.isdigit():
            return int(raw)
        else:
            print("请输入合法的整数（不能含字母或空格）")

def randnum(left: int, right: int) -> int:
    """生成指定范围内的随机整数"""
    return random.randint(left, right)

def guessing_game() -> None:
    print("🎯 欢迎来到猜数字小游戏！")
    
    # 获取范围
    left: int = parse_range_input("请输入随机数的起始值（整数）：")
    right: int = parse_range_input("请输入随机数的结束值（整数）：")

    if left >= right:
        print("❗ 起始值必须小于结束值，请重新运行程序！")
        return

    answer: int = randnum(left, right)
    attempts: int = 0

    print(f"\n我已经想好了一个 {left} 到 {right} 之间的整数，来猜猜吧！")

    while True:
        guess_input: str = input("请输入你的猜测：").strip()
        if not guess_input.isdigit():
            print("⚠️ 请输入有效的整数！")
            continue

        guess: int = int(guess_input)
        attempts += 1

        if guess < answer:
            print("太小啦～ 再试试！")
        elif guess > answer:
            print("太大啦～ 再试试！")
        else:
            print(f"🎉 恭喜你猜对了！答案就是 {answer}，你共猜了 {attempts} 次！")
            break

# 主程序入口
if __name__ == "__main__":
    guessing_game()
