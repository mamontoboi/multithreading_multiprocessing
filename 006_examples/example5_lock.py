# DEAD LOCK
import threading


def producer():
    print('Set locking')
    # беремо блокування
    with lock:
        print('done')
        # спроба взяти блокування у рамках поточного потоку дає нам DEAD LOCK
        # З цього блокування не вийти, оскільки ми очікуємо завершення
        # самого себе, щоб взяти блокування-блокування ніколи не звільниться.
        # Актуально навіть у рамках одного потоку
        with lock:
            print("It's great")
    print('Locking release!')


# блокування, що дозволяє відзначити якусь ділянку коду атомарною.
lock = threading.Lock()
# __enter__ => lock.acquire()
# __exit__ => lock.release()

task1 = threading.Thread(target=producer)
task2 = threading.Thread(target=producer)

task1.start()
task2.start()

task1.join()
task2.join()
