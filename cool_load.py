import os
from colorama import Fore, init

    
def process():
    """Симуляция процесса"""

    for i in range(5000000):
        i = 0


def cool_load(progress, load_width):
    """Выводит крутую полоску загрузки в зависимости от прогресса"""

    load_ready = int(load_width * (progress / 100))
    load = (
        '[', 
        Fore.GREEN + '+' * load_ready, 
        Fore.RED + '-' * (load_width - load_ready), 
        ']'
        )
    
    return load


def get_load_width():
    """Возвращает размер полоски загрузки, учитывая символы в стоке"""

    columns = os.get_terminal_size().columns
    return columns - 7


def clear():
    """Очистить консоль"""

    os.system('clear')


# Основная часть
init(autoreset=True)
clear()

if input("Начать загрузку вируса? (y / n) ") is 'y':
    pass
else:
    exit()

progress = 0
while progress < 100:
    process()
    progress += 1

    clear()
    print(f"\r{progress:<3}% ", *cool_load(progress, get_load_width()), sep='', end='')
else:
    print(Fore.MAGENTA + '\nВаш компьютер успешно заражён!')
