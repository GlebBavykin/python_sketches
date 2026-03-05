from typing import List, Optional


def bubblesort(array: List) -> List:
    """
         Bubble Sorti List
    """

    for row, _ in enumerate(array):
        # Последний элемент упорядочен
        last_element = len(array) - row - 1

        # Сортировать только те, что ещё не упорядочены
        for target in range(last_element):

            # Если текущий элемент больше следующего, то поменять их местами
            if array[target] > array[target + 1]:
                array[target], array[target + 1] = array[target + 1], array[target]
    return array


def selection_sort(array: List) -> List:
    """
        Selection Sort List
    """

    for i in range(len(array)):

        # Положим, что текущий элемент наименьший
        min_idx = i

        # Сравнить все элементы массива с текущим
        for j in range(i + 1, len(array)):

            # Если найдётся меньше, то он является наименьшим
            if array[min_idx] > array[j]:
                min_idx = j

        # Поменять местами текущий и наименьший элемент
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


def insertion_sort(array: List) -> List:
    """
        Insertion Sort List
    """

    for i in range(1, len(array)):

        # Берём текущее значение
        current = array[i]

        # Индекс последнего отсортированного элемента
        j = i - 1

        # Если последний отсортированный элемент больше текущего, то сдвинуть его вперёд
        while j >= 0 and current < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current
    return array


def quick_sort(array: List, low: int = 0, high: Optional[int] = None) -> List:
    """
        Quick Sort List
    """

    def partition(array: List, low: int, high: int) -> int:
        # Точка поворота на последнем элементе
        pivot = array[high]

        # Минимальный элемент находится перед первым элементом
        i = (low - 1)

        for j in range(low, high):

            # Выбрать только те, что меньше точки поворота
            if array[j] < pivot:
                # Теперь минимальный элемент на следующем месте
                i += 1
                # Поместить элемент меньше точки поворота на место минимального элемента
                array[i], array[j] = array[j], array[i]

        # Поместить точку поворота после минимального элемента
        array[i + 1], array[high] = array[high], array[i + 1]

        # Вывести индекс точки поворота в новом массиве
        return i + 1

    if high is None:
        high = len(array) - 1

    if low < high:
        # Упорядочить массив относительно точки поворота
        pivot = partition(array, low, high)

        # Упорядочить элементы слева от точки поворота
        quick_sort(array, low, pivot - 1)

        # Упорядочить элементы справа от точки поворота
        quick_sort(array, pivot + 1, high)
    return array


def merge_sort(array: List, left_index: Optional[int] = None, right_index: Optional[int] = None) -> List:
    """
        Merge Sort List
    """

    if left_index is None:
        left_index = 0

    if right_index is None:
        right_index = len(array)

    # Точка выхода из рекурсии: в массиве один элемент
    if left_index >= right_index:
        return

    # Вычислить середину массива
    middle = (left_index + right_index) // 2

    # Рекурсивно разделить левую часть
    merge_sort(array, left_index, middle)

    # Рекурсивно разделить правую часть
    merge_sort(array, middle + 1, right_index)

    # Слить элементы массива по возрастанию
    merge(array, left_index, right_index, middle)

    return array


def merge(array: List, left_index: int, right_index: int, middle: int) -> None:
    """
        Слить массива по возрастанию элементов
    """

    # Создать левую и правую копию массивов
    left_copy = array[left_index: middle + 1]
    right_copy = array[middle + 1: right_index + 1]

    # Инициализация индексов
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Пройти по двум копиям массивов
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # Если элемент слева меньше правого, то поместить его в отсортированный массив
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]

            # Сдвинуть индекс вперёд
            left_copy_index += 1
        else:
            # если элемент справа меньше левого, то поместить его в отсортированный массив
            array[sorted_index] = right_copy[right_copy_index]

            # Сдвинуть индекс вперёд
            right_copy_index += 1

            # Сдвинуть индекс отсортированного массива
        sorted_index += 1

    # Если в левой копии остались ещё элементы, то слить их в отсортированный массив
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1

    # Если в правой копии остались ещё элементы, то слить их в отсортированный массив
    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1
