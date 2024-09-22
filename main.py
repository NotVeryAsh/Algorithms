from math import floor
import datetime
import random


def bubble_sort(values):
    length = len(values)
    for i in range(0, length):
        for j in range(0, length - 1):
            current = values[j]
            comparison = values[j + 1]
            if comparison < current:
                values[j] = comparison
                values[j + 1] = current
    return values


def selection_sort(values):
    length = len(values)
    for i in range(0, length):
        smallest = i
        for j in range(i, length):
            if values[j] < values[smallest]:
                smallest = j
        temp = values[smallest]
        values[smallest] = values[i]
        values[i] = temp
    return values


def merge_sort(values):
    length = len(values)
    if length == 1:
        return values

    if length == 2:
        if values[0] < values[1]:
            return [values[0], values[1]]
        else:
            return [values[1], values[0]]

    middle = int(floor(len(values) / 2))

    left = []
    right = []

    for i in range(0, length):
        if i < middle:
            left.append(values[i])
        else:
            right.append(values[i])

    left = merge_sort(left)
    right = merge_sort(right)

    sorted_values = []

    for i in range(0, len(left) + len(right)):
        if len(left) == 0:
            sorted_values.append(right[0])
            right.pop(0)
            continue
        if len(right) == 0:
            sorted_values.append(left[0])
            left.pop(0)
            continue

        if left[0] < right[0]:
            sorted_values.append(left[0])
            left.pop(0)
        else:
            sorted_values.append(right[0])
            right.pop(0)

    return sorted_values


def linear_search(values, target):
    length = len(values)
    for i in range(0, length):
        if values[i] == target:
            return i
    return False


def binary_search(values, target):
    if len(values) == 0:
        return False

    if len(values) == 1 and values[0] != target:
        return False

    middle = int(floor(len(values) / 2))
    if values[middle] == target:
        return True

    min_index = 0
    max_index = len(values)

    if values[middle] < target:
        min_index = middle + 1
    else:
        max_index = middle

    new_values = []
    for i in range(min_index, max_index):
        new_values.append(values[i])

    return binary_search(new_values, target)


def generate_random_numbers():
    array = []
    while len(array) < 40000:
        number = random.randrange(1, 150000)
        array.append(number)
    return array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    random_numbers = generate_random_numbers()

    print("starting bubble sort...\n")
    before = datetime.datetime.now()
    bubble_sort(generate_random_numbers())
    after = datetime.datetime.now()
    c = after - before
    print("Time taken: ", c.total_seconds(), "\n")

    print("starting selection sort...\n")
    before = datetime.datetime.now()
    selection_sort(generate_random_numbers())
    after = datetime.datetime.now()
    c = after - before
    print("Time taken: ", c.total_seconds(), "\n")

    print("starting linear search...\n")
    before = datetime.datetime.now()
    print(linear_search(random_numbers, 1180))
    after = datetime.datetime.now()
    c = after - before
    print("Time taken: ", c.total_seconds(), "\n")

    print("starting binary search...\n")
    before = datetime.datetime.now()
    print(binary_search(random_numbers, 1180))
    after = datetime.datetime.now()
    c = after - before
    print("Time taken: ", c.total_seconds(), "\n")

    print("starting merge sort...\n")
    before = datetime.datetime.now()
    merge_sort(random_numbers)
    after = datetime.datetime.now()
    c = after - before
    print("Time taken: ", c.total_seconds(), "\n")
