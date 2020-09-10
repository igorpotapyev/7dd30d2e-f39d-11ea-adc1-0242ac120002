# Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения. 


def elems_from_first_list_not_second_n_n(lst1, lst2):
    # create hash sets from lists
    # space complexity: O(n + n) ~= O(n) [creating two new collections]
    # time complexity: O(n + n) ~= O(n) [O(n) to iterate over the each list]
    set1 = set(lst1)
    set2 = set(lst2)
    
    # calc difference
    # space complexity: O(n) [creating new collection]
    # time complexity: O(n) [more precisely O(len(set1))]
    set3 = set1 - set2

    # result complexity:
    # space complexity: O(n + n) ~= O(n)
    # time complexity: O(n + n) ~= O(n)
    return set3


def elems_from_first_list_not_second_1_n2(lst1, lst2):
    lst3 = []

    ind = 0
    while(ind < len(lst1)):  # time complexity O(n)
        found_elem = False
        l1 = lst1[ind]
        for l2 in lst2:  # time complexity ~O(n)
            if l1 == l2:
                found_elem = True
                break
        if found_elem:
            lst1.remove(l1)
        else:
            ind += 1

    # result complexity:
    # space complexity: O(1) [no need to create new collection]
    # time complexity: O(n^2) [inner iterations]

    return lst1


if __name__ == '__main__':
    lst1 = [1,2,3,4,5,6]
    lst2 = [3,4,5,6,7,8]
    lst3 = elems_from_first_list_not_second_n_n(lst1, lst2)
    assert lst3 == {1, 2}

    lst1 = [1,2,3,4,5,6]
    lst2 = [3,4,5,6,7,8]
    lst3 = elems_from_first_list_not_second_1_n2(lst1, lst2)
    assert lst3 == [1,2]

    print('Success!')
