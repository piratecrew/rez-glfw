# -*- coding: utf-8 -*-

name = 'glfw'

version = '3.2.1'

authors = ['frbr']

def commands():
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

