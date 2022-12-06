import threading

# кількість мереж активних потоків
print(threading.active_count())
# поточний потік
current = threading.current_thread()
# ім'я поточного потоку
print(current.name)
# перевірка стану потоку - живий чи ні
print(current.is_alive())
# що станеться, якщо спробуємо ще раз його запустити
try:
    # Потік може бути запущений лише раз
    current.start()
except RuntimeError as e:
    # отримуємо виняток, оскільки основний потік працює
    print('ERROR: {error}'.format(error=e))
current.name = 'SuperThread'
print(current.name)

# насправді setName, getName – це просто старий інтерфейс.
# У реальних завданнях ви можете працювати безпосередньо з атрибутом name
current.name = 'SuperThread1'
print(current.name)

# виведення всіх занедбаних і живих тредів
print(threading.enumerate())

# Напишемо приклад демонстрації потокобезпечного сховища даних.
thread_data = threading.local()
thread_data.value = 5


def print_results():
    """
    Виконуючи цю функцію в різних потоках, ми помітимо, що сховище дійсно має різні значення
    в рамках кожного потоку - звідси і назва потокобезпечного сховища.
    :return:
    """
    print(threading.current_thread())
    print('Result: {}'.format(thread_data.value))


def counter(started, to_value):
    print(hasattr(thread_data, 'value'))
    thread_data.value = started
    for i in range(to_value):
        thread_data.value += 1
    print_results()


# запускаємо потоки, у яких змінюємо значення thread_data.value
task1 = threading.Thread(target=counter, args=(0, 10), name='Task1')
task2 = threading.Thread(target=counter, args=(100, 3), name='Task2')
task1.name = 'task1'
task2.name = 'task2'

task1.start()
task2.start()

print_results()

task1.join()
task2.join()
print_results()
