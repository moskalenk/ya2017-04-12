import os

task = '''
Реализуйте сортировку слиянием для одномерного массива.
Сложность алгоритма должна быть не хуже, чем O(n log n)

Первая строка содержит число 1<=n<=10000,
вторая - массив A[1…n], содержащий натуральные числа, не превосходящие 10E9.
Необходимо отсортировать полученный массив.

Sample Input:
5
2 3 9 2 9
Sample Output:
2 2 3 9 9
'''


def mergeSort(m):
    # ваше решение


    return


def main():
    fn = os.path.dirname(os.path.abspath(__file__)) + "/dataB.txt"
    f = open(fn)
    size = int(f.readline().replace("\n", ""))
    strings = f.readline().replace("\n", "").split(" ")
    array = list(map(int, strings))
    assert size==len(array)

    print(" array=", array)
    sort=mergeSort(array)
    print(" sort=", sort)


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
