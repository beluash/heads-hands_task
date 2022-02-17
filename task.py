# Python 3.7.12

import random

#вспомогательные функции

def create_arrays(n):
  ar = []
  sizes = []
  for i in range(n):
    num = random.randint(1, 100) 
    while (num in sizes):
      num = random.randint(1, 100)
    ar.append([random.randint(1, 100000) for i in range(num)])
    sizes.append(num)
  return ar

def sort_arrays(ar, n):
  for i in range(n):
    if i % 2 == 0: ar[i].sort()
    else: ar[i].sort(reverse=True)

# функция для задания
      
def task(n):
  ar = create_arrays(n)
  sort_arrays(ar, n)
  return ar


# Вопросы по формулировке задания:
# 1) Какие ограничения на размеры массива? В данном решении размер массива находится в диапазоне от 1 до 100.  
# 2) Какие ограничения на максимальное число для заполнения массива? В данном решении исползуются числа в диапазоне от 1 до 100000.
# 3) Можно ли было использовать встроенные функции сортировки? В данном решении они используются. 
