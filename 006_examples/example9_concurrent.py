from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def handler(started=0, finished=0):
    # print('VALUES', started, finished)
    result = 0
    for i in range(started, finished):
        result += i
    return result


def run_by_executor(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    # створюємо футури і виконуємо паралельно (не забуваємо про GIL + threads).
    # executor.submit дозволяє відправити функцію виконання в pool.
    future1 = executor.submit(handler, started=0, finished=2 ** 26)
    future2 = executor.submit(handler, started=2 ** 26, finished=2 ** 28)

    result = future2.result() + future1.result()
    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


def run_by_executor_map(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()
    params = [
        [0, 2 ** 26],
        [2 ** 26, 2 ** 28]
    ]
    # використовуючи map, запускає функцію handler на наборах даних params
    # в результаті executor.map поверне нам список результатів, який ми можемо підсумувати.
    # Зручніше, ніж executor.submit у тому випадку, якщо нам не потрібна футури для окремих наборів даних.
    result = sum(executor.map(handler, *params))

    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=result,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


# порівняємо багатопоточне виконання та багатопроцесне
print('Execute using map...')
run_by_executor_map(ThreadPoolExecutor)
run_by_executor_map(ProcessPoolExecutor)

print('Execute using submit...')
run_by_executor(ThreadPoolExecutor)
run_by_executor(ProcessPoolExecutor)
