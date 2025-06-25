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
                'type': type(obj).__name__,  # __name__属性返回对象的类名字符串
                'value': obj,
                'doc': obj.__doc__  # __doc__属性返回对象的文档字符串
            }
            return info_dict

    def check_all_attribute(self):
        # 这种初始话+条件分支处理似乎属于"EAFP"（Easier to Ask for Forgiveness than Permission）
        attr__all__dict = {
            'has_all': False,
            'all_items': [],
            'all_count': 0,
        }
        if hasattr(self.module, '__all__'):
            attr__all__dict['has_all'] = True
            attr__all__dict['all_items'] = self.module.__all__
            attr__all__dict['all_count'] = len(self.module.__all__)
        return attr__all__dict

    def get_item_info_new(self, item_name: str) -> dict:
        obj = getattr(self.module, item_name)
        info_dict = {
            'name': obj.__name__,
            'value': obj,
            'doc': obj.__doc__,  # __doc__属性返回对象的文档字符串
            'type': type(obj).__name__,  # __name__属性返回对象的类名字符串
            'types': type(obj)
        }
        return info_dict


if __name__ == '__main__':
    pak_name = 'math'
    Explorer = LibraryExplorer(pak_name)
    print(Explorer.separate_by_type())
    print(Explorer.get_item_info('pi'))
