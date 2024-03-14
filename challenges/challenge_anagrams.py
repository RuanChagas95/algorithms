def binary_search(arr: list, element: int,
                  min_index: int, max_index: int) -> int:
    while min_index != max_index:
        point_index = (min_index + max_index) // 2
        if element > arr[point_index]["value"]:
            min_index = point_index + 1
        else:
            max_index = point_index
    return min_index


def find_index(arr: list, element: int, min_index: int, max_index: int) -> int:
    if arr[min_index + 1]["value"] >= element:
        return min_index
    if arr[max_index - 1]["value"] <= element:
        return max_index
    return binary_search(arr, element, min_index + 2, max_index - 1)


def update_arr(element, index, new_order, arr):
    new_order[index] = {"value": element, "deep": []}
    arr[index] = element


def partialSort(orded: dict, first: int, arr: list) -> dict:
    index = 0
    new_order = {}

    for index_order in range(len(orded)):
        new_order_index = index_order + first
        deep = orded[new_order_index]["deep"]
        if len(deep) > 0:
            if len(deep) > 1:
                my_sort(deep)
            for element in deep:
                update_arr(element, index, new_order, arr)
                index += 1
        update_arr(orded[new_order_index]["value"], index, new_order, arr)
        index += 1

    return new_order


def build_ordered_structure(arr: list) -> dict:
    ordered_structure = {0: {"value": arr[0], "deep": []}}
    min_index = -1
    max_index = 1
    for i in range(1, len(arr)):
        index = find_index(ordered_structure, arr[i], min_index, max_index)
        if index not in ordered_structure:
            ordered_structure[index] = {"value": arr[i], "deep": []}
            if index == min_index:
                min_index -= 1
            else:
                max_index += 1
        else:
            ordered_structure[index]["deep"].append(arr[i])
            if len(ordered_structure[index]["deep"]) > len(ordered_structure):
                ordered_structure = partialSort(
                    ordered_structure, min_index + 1, arr)
                max_index = len(ordered_structure)
                min_index = -1
    partialSort(ordered_structure, min_index + 1, arr)
    return ordered_structure


def my_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    build_ordered_structure(arr)
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
