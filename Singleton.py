#coding=utf-8
from functools import wraps, partial
from functools import wraps

"""    单例模式的实现（线程友好）"""
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass
        
    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)  
        return Singleton._instance
# --------------------------------方法二，装饰器
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x    
        
# -------------------------------方法三，模块
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
使用from module import singleton
    
