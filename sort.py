# -*- coding: utf-8 -*-

"""
Функции фозвращают новые объекты list, тк "родной"
питонячий sorted тоже возвращают новый объект
"""


def cocktail(array: list, *, reverse: bool = False) -> list:
    """Сортировка перемешиванием"""
    array = list(array)

    left_position = 0
    right_position = len(array) - 1

    while left_position <= right_position:
        for index in range(left_position, right_position):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]

        right_position -= 1

        for index in range(right_position, left_position, -1):
            if array[index - 1] > array[index]:
                array[index], array[index - 1] = array[index - 1], array[index]

        left_position += 1

    return array[::-1] if reverse else array


def bobble(array: list, *, reverse: bool = False) -> list:
    """Сортировка пузырьком"""
    array = list(array)

    left_position = 0
    right_position = len(array) - 1

    while left_position <= right_position:
        index = 0

        while index < right_position - left_position:
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]

            index += 1

        left_position += 1

    return array[::-1] if reverse else array


def insertion(array: list, *, reverse: bool = False) -> list:
    """Сортировка вставками"""
    array = list(array)

    for right_position in range(1, len(array)):
        value = array[right_position]
        left_position = right_position - 1

        while left_position >= 0 and value < array[left_position]:
            array[left_position + 1] = array[left_position]
            left_position -= 1

        array[left_position + 1] = value

    return array[::-1] if reverse else array


if __name__ == '__main__':
    from random import randint

    def _create_random_array(num=30):
        return [randint(-99, 99) for _ in range(num)]

    func_to_example = (
        (cocktail, _create_random_array()),
        (bobble, _create_random_array()),
        (insertion, _create_random_array()),
    )

    for func, example in func_to_example:
        print(f'{func.__doc__}:'.upper())
        print(example)
        print('Without reverse:')
        print(func(example))
        print('With reverse:')
        print(func(example, reverse=True))
