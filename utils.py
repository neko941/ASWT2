import os

def advanced_flatten_list(alist):
    flattened_list = []
    for element in alist:
        if isinstance(element, list):
            flattened_list.extend(advanced_flatten_list(element))
        else:
            flattened_list.append(element)
    return flattened_list

def advanced_path_join(alist):
    return os.path.join(*advanced_flatten_list(alist))

def _advanced_mkdir(func):
    def wrap(a):
        if isinstance(a, list):
            func(a)
        else:
            func([a])
    return wrap
@_advanced_mkdir
def advanced_mkdir(dir_list):
    for dir in dir_list:
        dirs = []
        while True:
            if not os.path.exists(dir):
                arr = os.path.normpath(dir).split(os.sep)
                dirs.insert(0, arr[-1])
                dir = advanced_path_join(arr[:-1])
            else:
                for i in range(len(dirs)):
                    os.mkdir(advanced_path_join([dir, dirs[:i+1]]))
                break