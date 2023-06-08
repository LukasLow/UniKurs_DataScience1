import matplotlib.pyplot as plt
import pytest

from merge_sort import mergeSort, ASSIGNMENT


def test_mergeSort():
    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    expected_sorted_list = [17, 20, 26, 31, 44, 54, 55, 77, 93]

    mergeSort(my_list)
    assert my_list == expected_sorted_list

    # Test with an empty list
    empty_list = []
    mergeSort(empty_list)
    assert empty_list == []

    # Test with a list of one element
    single_element_list = [42]
    mergeSort(single_element_list)
    assert single_element_list == [42]


if __name__ == "__main__":
    pytest.main()
