#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


if __name__ == "__main__":
    path = "C:/Users/Evil/PycharmProjects"
    dir_list = os.listdir(path)
    print("Files and directories in '", path, "' :")
    print(dir_list)
