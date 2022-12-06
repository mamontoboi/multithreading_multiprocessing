# Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!».
# Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу.
# Якщо файл є, то відкриває його і шукає рядок «Wow!». За наявності цього рядка закриває файл і генерує подію,
# а інша функція чекає на цю подію і у разі її виникнення виконує видалення цього файлу. Якщо рядки «Wow!» не було
# знайдено у файлі, то засипати на 5 секунд. Створіть файл руками та перевірте виконання програми.

import time
import os
import threading


# читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!»
def reader(file_name):
    try:
        file = open(file_name, 'r')
        # Якщо файл є, то відкриває його і шукає рядок «Wow!»
        if "Wow!" in file.read():
            print('Wow! was found!')
            # За наявності цього рядка закриває файл і генерує подію
            file.close()
            product.set()
            product.clear()
        # Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд.
        else:
            print(f"Wow! wasn't found in {file_name}!")
            file.close()
            time.sleep(5)
    # Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу.
    except:
        print(f"File {file_name} wasn't found! \nReader is sleeping.")
        time.sleep(5)
        reader(file_name)


def deleter(file_name):
    # чекає на цю подію і у разі її виникнення виконує видалення цього файлу
    product.wait()
    start_files = os.listdir('.')
    print(f"The initial files in the directory are: {', '.join(start_files)}")
    os.remove(file_name)
    print("Deleter is starting.")
    end_files = os.listdir('.')
    print(f"The remaining files in the directory are: {', '.join(end_files)}")
    creation_product.set()
    creation_product.clear()


def creator(file_name):
    creation_product.wait()
    with open(file_name, 'w') as file:
        print(f'New file {file_name} was created.')
        file.write('Wow!')


product = threading.Event()
creation_product = threading.Event()

task1 = threading.Thread(target=reader, args=['It.txt'])
task2 = threading.Thread(target=deleter, args=['It.txt'])
task3 = threading.Thread(target=creator, args=['It.txt'])

task1.start()
task2.start()
task3.start()

task1.join()
task2.join()
task3.join()
