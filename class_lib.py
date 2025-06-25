# -*- coding: utf-8 -*-
"""
Created on 2025/6/23 3:12

@author: Jia Yuxuan
"""
import importlib
import inspect


def is_magic(attr_name: str)->bool:
    if len(attr_name) < 4:
        return False
    if attr_name[:2] != '__' or attr_name[-2:] != '__':
        return False
    return True


def safe_get(obj, attr_name: str) -> str|dict:
    try:
        return getattr(obj, attr_name)
    except Exception as e:
        return {
            'error': type(e).__name__,  # 获取错误类型名称，例如 AttributeError
            'message': str(e)  # 获取错误信息字符串
        }


class LibraryExplorer:
    def __init__(self, module_name):
        self.module = importlib.import_module(module_name)

    def list_all_items(self) -> list:
        return dir(self.module)

    def count_items(self) -> int:
        return len(dir(self.module))

    def separate_by_type(self) -> dict:
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

    def get_item_info(self, item_name: str) -> dict:
        obj = getattr(self.module, item_name)
        info_dict = {
            'name': item_name,
            'value': obj,
            'type': type(obj).__name__,  # __name__属性返回对象的类名字符串
            '__name__': safe_get(obj, '__name__'),
            '__doc__': safe_get(obj, '__doc__'),  # __doc__属性返回对象的文档字符串
            '__module__': safe_get(obj, '__module__'),
            '__package__': safe_get(obj, '__package__'),

        }
        return info_dict

    def get_summary_info(self) -> dict:
        summary_dict = {}
        for item_name in self.list_all_items():
            summary_dict[item_name] = self.get_item_info(item_name)
        return summary_dict

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


if __name__ == '__main__':
    pak_name = 'math'
    Explorer = LibraryExplorer(pak_name)

