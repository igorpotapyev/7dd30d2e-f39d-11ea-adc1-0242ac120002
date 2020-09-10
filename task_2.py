# Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.


def remove_zeros(arr_input):
    ind = 0
    while(ind < len(arr_input)):  # len() for list has O(1) time complexity
        val = arr_input[ind]
        if val == 0:
            arr_input.remove(val)  # list.remove() has O(n) time complexity, O(1) space complexity
        else:
            ind += 1


if __name__ == '__main__':
    array_input = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]
    array_check = [1, 4, 5, 6, 7, 8, -4]
    remove_zeros(array_input)
    assert array_input == array_check

    array_input = [0, 0, 0]
    array_check = []
    remove_zeros(array_input)
    assert array_input == array_check

    array_input = []
    array_check = []
    remove_zeros(array_input)
    assert array_input == array_check

    array_input = [-1, 2, -3]
    array_check = [-1, 2, -3]
    remove_zeros(array_input)
    assert array_input == array_check

    array_input = [0, -1]
    array_check = [-1]
    remove_zeros(array_input)
    assert array_input == array_check    

    array_input = [-1, 0]
    array_check = [-1]
    remove_zeros(array_input)
    assert array_input == array_check

    print('Success!')
