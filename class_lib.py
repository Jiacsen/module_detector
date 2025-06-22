# -*- coding: utf-8 -*-
"""
Created on 2025/6/23 3:12

@author: Jia Yuxuan
"""
import importlib


class LibraryExplorer:
    def __init__(self, module_name):
        self.module = importlib.import_module(module_name)

    def list_all_items(self):
        return dir(self.module)

    def count_items(self):
        return len(dir(self.module))


if __name__ == '__main__':
    pak_name = 'math'
    Explorer = LibraryExplorer(pak_name)
    print(Explorer.list_all_items())
    print(Explorer.count_items())
