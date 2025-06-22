# -*- coding: utf-8 -*-
"""
Created on 2025/6/23 3:12

@author: Jia Yuxuan
"""
class LibraryExplorer:
    def __init__(self, pak_name):
        self.num_of_dir: int
        self.att_and_med: list[str]

    def list_all_items(self, pak_name):
        return dir(pak_name)

    def count_items(self, pkg_name):
        return len(dir(pkg_name))


if __name__ == '__main__':
    import math
    pak = math
    LibraryExplorer = LibraryExplorer(pak)
    print(LibraryExplorer.list_all_items(pak))
    print(LibraryExplorer.count_items(pak))
