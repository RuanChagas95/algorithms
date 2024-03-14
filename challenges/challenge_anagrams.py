def find_index(arr: list, element: int, min, max) -> int:
    prev_point_index = None
    if (arr[min + 1]["value"] >= element):
        return min
    if (arr[max - 1]["value"] <= element):
        return max
    min += 2
    max -= 1
    while (min != max):
        point_index = int((min + max) / 2)
        if (prev_point_index == point_index):
            if (prev_point_index == min):
                point_index += 1
            else:
                point_index -= 1
        prev_point_index = point_index
        major = element >= arr.get(point_index, {}).get("value", float('-inf'))
        equal = element == arr.get(point_index, {}).get("value", float('-inf'))
        if (major and not equal):
            min = point_index + 1
        elif (not major and not equal):
            max = point_index
        elif (equal):
            return point_index
        else:
            min = point_index
    return min


def partialSort(orded: dict, first: int, arr: list) -> dict:
    index = 0
    new_order = {}

    def update_arr(element):
        nonlocal index
        new_order[index] = {"value": element, "deep": []}
        arr[index] = element
        index += 1
    for index_order in range(len(orded)):
        new_order_index = index_order + first
        deep = orded[new_order_index]["deep"]
        if (len(deep) > 0):
            if (len(deep) > 1):
                my_sort(deep)
            for element in deep:
                update_arr(element)
        update_arr(orded[new_order_index]["value"])
    return new_order


def my_sort(arr: list) -> list:
    if (len(arr) < 2):
        return arr
    orded = {0: {"value": arr[0], "deep": []}}
    min = -1
    max = 1
    for i in range(1, len(arr)):
        index = find_index(orded, arr[i], min, max)
        if ((index not in orded)):
            orded[index] = {"value": arr[i], "deep": []}
            if (index == min):
                min -= 1
            else:
                max += 1
        else:
            orded[index]["deep"].append(arr[i])
            if (len(orded[index]["deep"]) > len(orded)):
                orded = partialSort(orded, min + 1, arr)
                max = len(orded)
                min = -1
    partialSort(orded, min + 1, arr)
    return arr


def is_anagram(first_string, second_string):
    if (len(first_string) == 0 and len(second_string) == 0):
        return (first_string, second_string, False)
    first_orded = ''.join(my_sort(list(first_string.lower())))
    second_orded = ''.join(my_sort(list(second_string.lower())))
    if (len(first_string) != len(second_string)):
        return (first_orded, second_orded, False)
    if (first_orded == second_orded):
        return (first_orded, second_orded, True)
    else:
        return (first_orded, second_orded, False)


if (__name__ == "__main__"):
    assert is_anagram("hello", "lehlo")[2]
    assert is_anagram("hello", "leh_ol")[2] is False
    assert is_anagram("f", "F")[2]
    assert is_anagram("", "")[2] is False
    assert is_anagram('aaeeiioouu', 'aaiiiioouu')[2] is False
