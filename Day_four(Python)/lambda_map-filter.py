'''
✅ 小型巩固练习项目：【数据清洗小工具】
🌟 需求：

输入一组带有负数和重复元素的列表

使用 列表推导式 清理掉负数

使用 集合推导式 去重

使用 map + lambda 将所有数平方

最后生成一个字典：元素值 → 该元素的位数（用字典推导式）
'''

def data_cleaning(nums: list) -> dict:
    # 1. 清理负数并去重
    cleaned = {x for x in nums if x >= 0}
    
    # 2. 平方处理
    squared = list(map(lambda x: x ** 2, cleaned))
    
    # 3. 转为 字典：数值 → 位数
    result = {num: len(str(num)) for num in squared}
    
    return result
