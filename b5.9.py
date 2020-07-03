"функция-декоратор, измеряющая время выполнения другой функции"
def how_long(pol):
    def func_run(func):
        import time
        def func_wrapper(i):
            result = 0
            for once in range(pol):
                t0 = time.time()
                func(i)
                t1 = time.time()
                rt = t1 - t0
                result += rt
            result /= pol
            print(result)
        return func_wrapper
    return func_run

"пример реализации"
@how_long(10)
def fibonacci(n):
    a, b = 1, 2
    while a < n:
        print(a, end=" ")
        a, b = b, b + a
    print()

fibonacci(400)


