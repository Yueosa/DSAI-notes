def add_fruit(stock: dict):
    name = input("请输入水果名称：").strip()
    if name in stock:
        print("该水果已存在，当前库存为", stock[name])
        return
    try:
        count = int(input("请输入库存数量："))
        stock[name] = count
        print("✅ 添加成功！")
    except ValueError:
        print("❗ 数量必须是整数")

def update_fruit(stock: dict):
    name = input("请输入要修改的水果：").strip()
    if name not in stock:
        print("❌ 没有这个水果")
        return
    try:
        count = int(input("请输入新数量："))
        stock[name] = count
        print("✅ 修改成功")
    except ValueError:
        print("❗ 数量必须是整数")

def delete_fruit(stock: dict):
    name = input("请输入要删除的水果：").strip()
    if name in stock:
        del stock[name]
        print("✅ 删除成功")
    else:
        print("❌ 没有这个水果")

def query_fruit(stock: dict):
    for k, v in stock.items():
        print(f"{k}：{v}个")

def main():
    stock = {}
    while True:
        print("""
====== 水果库存系统 ======
1. 添加水果
2. 修改库存
3. 删除水果
4. 查看所有
0. 退出
""")
        choice = input("请选择操作：").strip()
        if choice == "1":
            add_fruit(stock)
        elif choice == "2":
            update_fruit(stock)
        elif choice == "3":
            delete_fruit(stock)
        elif choice == "4":
            query_fruit(stock)
        elif choice == "0":
            print("🍓 再见啦~")
            break
        else:
            print("⚠️ 输入无效，请重新选择")

main()
