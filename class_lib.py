# -*- coding: utf-8 -*-
"""
Created on 2025/6/23 3:12

@author: Jia Yuxuan
"""
import importlib
import inspect

def is_magic(name):
    if len(name) < 4:
        return False
    if name[:2] != '__' or name[-2:] != '__':
        return False
    return True

class LibraryExplorer:
    def __init__(self, module_name):
        self.module = importlib.import_module(module_name)

    def list_all_items(self):
        return dir(self.module)

    def count_items(self):
        return len(dir(self.module))

    def separate_by_type(self):
        types_dict = {
            'functions': [],
            'classes': [],
            'special': [],
            'variables': []
        }
        for item_name in self.list_all_items():
            obj = getattr(self.module, item_name)
            if inspect.isclass(obj):  # 首先判断是否为类
                types_dict['classes'].append(item_name)
            elif callable(obj):  # 根据是否为可调用对象判断是否为函数，类也是可调用对象，但已经在上一步判断过了
                types_dict['functions'].append(item_name)
            elif is_magic(item_name):  # TODO: 这里的判断还不够准确，需要进一步完善，暂时忽略
                types_dict['special'].append(item_name)
            else:
                types_dict['variables'].append(item_name)
        return types_dict

    def get_item_info(self, item_name):
        if not item_name in self.list_all_items():
            print('Item not found.')
            return None
        else:
            obj = getattr(self.module, item_name)
            info_dict = {
                'name': item_name,
                'type': type(obj).__name__,
                'value': obj,
                'doc': obj.__doc__
            }
            return info_dict


if __name__ == '__main__':
    pak_name = 'math'
    Explorer = LibraryExplorer(pak_name)
    print(Explorer.separate_by_type())
    print(Explorer.get_item_info('pi'))
