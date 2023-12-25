#!D:/Application/python/python.exe
# 斐波那契数列

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} 执行时间: {elapsed_time:.4f} 秒")
        return result
    return wrapper

# 使用装饰器
@timing_decorator
def example_function():
    # 模拟一些耗时的操作
    time.sleep(2)
    print("Function completed.")

# 调用被装饰的函数
example_function()