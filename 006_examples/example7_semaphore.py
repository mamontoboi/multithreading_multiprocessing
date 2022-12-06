import threading
import time


def producer():
    with lock:
        # виведемо скільки разів можна буде взяти семафор: це внутрішній лічильник
        print('Set locking', lock._value)
        time.sleep(3)
        print("I'm free")


# семафор - дозволяє взяти блокування значення разів і не більше.
# можна змінити max_workers на 2 і порівняти поведінку.
max_workers = 3
lock = threading.BoundedSemaphore(value=max_workers)  # starts several threads at the same time

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)
task3 = threading.Thread(target=producer)
task4 = threading.Thread(target=producer)

task1.start()
task2.start()
task3.start()
task4.start()

task1.join()
task2.join()
task3.join()
task4.join()
