import random
import string

n = 4
size = 10

def fill_rand_arr(size):
    all_symbols = string.ascii_letters + string.digits + "!@#$%^&*"
    array = []
    for _ in range(size):
        rand_elem_size = random.randint(1, 8)
        rand_str = ''.join(random.choice(all_symbols) for _ in range(rand_elem_size))
        array.append(rand_str)
    return array

def get_size_of_second_array(arr):
    second_size = sum(1 for s in arr if len(s) < n)
    return second_size

def rotate_elem_of_arr(arr):
    array_two = [s for s in arr if len(s) < n]
    return array_two

array_one = fill_rand_arr(size)
if get_size_of_second_array(array_one) == 0:
    print("Искомых элементов строкового массива для переноса в новый массив - нет")
else:
    print("Перед вами строковый массив, заполненный случайными значениями, и новый массив, впитавший в себя элементы предыдущего массива, длина которых равна трём или менее символов:")
    array_two = rotate_elem_of_arr(array_one)
    print(f"[{', '.join(array_one)}] -> [{', '.join(array_two)}]")
