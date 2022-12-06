# Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread,
# і заміряйте швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же
# набір завдань на ThreadPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до
# максимально можливих, щоб побачити приріст або втрату продуктивності.

import threading
import concurrent.futures
import time
from random import randint


def factorial(num):
    # print(f'Calculating factorial of {num}')
    total = sum(range(1, num + 1))
    # print(f'Factorial of {num} equals {total}')


def thdng(lst: list):
    """
    :param lst: list of numbers, factorial of which to be found.
    :return: total time of operation
    """
    start = time.perf_counter()
    threads = []
    for i in lst:
        task = threading.Thread(target=factorial, args=[i])
        task.start()
        threads.append(task)
    for thread in threads:
        thread.join()
    end = time.perf_counter()

    print(f'Total time of calculation using threading method is {round(end - start, 4)} seconds')


def tpe(lst: list):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(factorial, lst)

    end = time.perf_counter()

    print(f'Total time of calculation using ThreadPoolExecutor method is {round(end - start, 4)} seconds')


def ppe(lst: list):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(factorial, lst)

    end = time.perf_counter()

    print(f'Total time of calculation using ProcessPoolExecutor method is {round(end - start, 4)} seconds')


numbs = []
for i in range(1000):
    numbs.append(randint(100, 1000000))

if __name__ == '__main__':
    thdng(numbs)
    tpe(numbs)
    ppe(numbs)
