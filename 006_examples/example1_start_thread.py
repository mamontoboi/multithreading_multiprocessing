import threading
import time


def handler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    print('Value: ', result)


params = {'finished': 2 ** 26}

# попереднє створення потоку, який виконуватиме обробник функції,
# з ключовими аргументами params.
task = threading.Thread(target=handler, kwargs=params)
started_at = time.time()
print('RESULTS 1')
# запускаємо потік виконання
task.start()
# приєднуємо потік до поточного-тобто ми як би синхронізуємо другий потік,
# чекаючи від нього результату
task.join()
print('Time: {}'.format(time.time() - started_at))

started_at = time.time()
print('RESULTS 2')
handler(**params)
print('Time: {}'.format(time.time() - started_at))
