# check.py

# # ВАРИАНТ 1
# elements_count = int(input())
# data = [input() for _ in range(elements_count)]
# print(data)

# # ВАРИАНТ 2
# import datetime

# # Чтение входных данных
# elements_count = int(input())
# data = [input() for _ in range(elements_count)]

# # Запись в файл с временными метками
# with open('output.txt', 'a', encoding='utf-8') as f:
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     f.write(f"{timestamp}\n")
#     f.write(f"{data}\n")
#     f.write("\n")  # пустая строка для разделения запусков

# # Вывод на экран
# print(data)


# ВАРИАНТ 3
import datetime
import sys

# Чтение входных данных из stdin
elements_count = int(sys.stdin.readline().rstrip())
data = [sys.stdin.readline().rstrip() for _ in range(elements_count)]

# Запись в файл с временными метками
with open('output.txt', 'a', encoding='utf-8') as f:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{timestamp}\n")
    f.write(f"{data}\n")
    f.write("\n")  # пустая строка для разделения запусков

# Вывод на экран
print(data)
