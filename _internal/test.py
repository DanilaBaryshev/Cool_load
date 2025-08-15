import os
import sys
from colorama import Fore, init


# Проверяем, запущен ли скрипт из терминала
if not sys.stdin.isatty():
    # Берем путь до исходного скрипта
    script_path = os.path.abspath(__file__)
    # Открываем новый терминал и запускаем скрипт
    os.system(f'gnome-terminal -- bash -c "python3 \\"{script_path}\\"; exec bash"')
    sys.exit()

    
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


def clear():
    """Очистить консоль"""
    os.system('clear')


# Основная часть
init(autoreset=True)

LOAD_WIDTH = int(input("Введите размер полоски загрузки (стандарт 40): "))
if LOAD_WIDTH > 73:
    LOAD_WIDTH = 73

clear()
progress = 0
while progress < 100:
    process()
    progress += 1
    print(f"\r{progress:<3}% ", *cool_load(progress, LOAD_WIDTH), sep='', end='')
else:
    print(Fore.YELLOW + '\nThe process is ready!')