# DEAD LOCK
import threading


def producer():
    print('Set locking')
    with lock:
        # потік, що взяв блокування може взяти її нескінченну кількість разів.
        # але інший потік чекатиме
        with lock:
            print("It's great")
    print('Locking release!')


# приклад аналогічний example5_lock.py, але вирішує проблему DEAD LOCK у рамках одного потоку.
lock = threading.RLock()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
