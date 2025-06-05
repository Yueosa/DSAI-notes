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
    """
    作用: 通過三步處理, 返回期望字典

    參數:
        nums: 需要去重的列表
    
    處理:
        (1) 使用 集合推導式, 篩選出所有 不爲複的值
        (2) 使用 lambda 對所有數進行 平方 操作, 使用 list() 將 map() 實現並消耗
        (3) 使用 字典推導式 返回數字和位數的 鍵值對
    """
    cleaned = {x for x in nums if x >= 0}
    
    squared = list(map(lambda x: x ** 2, cleaned))
    
    result = {num: len(str(num)) for num in squared}
    
    return result

if __name__ == '__main__':
    nums: list = [1, -23, 91, 226, -706, 847]
    result: dict = data_cleaning(nums)
    print(result)
