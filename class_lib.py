# -*- coding: utf-8 -*-
"""
Created on 2025/6/23 3:12

@author: Jia Yuxuan
"""
import importlib
import inspect


# TODO:第二个学习任务
# 现在你已经掌握了基础，让我们增加功能。下一个任务：
# 为LibraryExplorer类添加两个新方法：
# 1.
# separate_by_type() - 返回一个字典，将模块中的项目按类型分类：
#
# 键：'functions'（函数）、'classes'（类）、'variables'（变量/常量）
# 值：对应类型的项目名称列表
#
# 2.
# get_item_info(item_name) - 接收一个项目名称，返回该项目的详细信息（类型、值等）
#
# 学习提示：
#
# 使用callable()检查是否为可调用对象（函数/方法）
# 使用inspect.isclass()检查是否为类（需要import inspect）
# 使用getattr()获取对象的属性值
# 考虑异常处理：如果项目名称不存在怎么办？
class LibraryExplorer:
    def __init__(self, module_name):
        self.module = importlib.import_module(module_name)

    def list_all_items(self):
        return dir(self.module)

    def count_items(self):
        return len(dir(self.module))

    def separate_by_type(self):
        types_dict = {'functions': [], 'classes': [], 'variables': []}
        for item_name in self.list_all_items():
            if inspect.isclass(getattr(self.module, item_name)):  # 首先判断是否为类
                types_dict['classes'].append(item_name)
            elif callable(getattr(self.module, item_name)):  # 根据是否为可调用对象判断是否为函数，类也是可调用对象，但已经在上一步判断过了
                types_dict['functions'].append(item_name)
            else:
                types_dict['variables'].append(item_name)
        return types_dict


if __name__ == '__main__':
    pak_name = 'math'
    Explorer = LibraryExplorer(pak_name)
    print(Explorer.list_all_items())
    print(Explorer.count_items())
