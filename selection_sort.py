import unittest
import random


#defined function
def selection_sort(arr):
    # Check for arrays with 1 element or less
    if len(arr) <= 1:
        return
    # iterate through all array elements
    for i in range(len(arr)):
        #find the min element in the remaining unsorted
        min_index = i
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap the found min with the element at the current location
        arr[i], arr[min_index] = arr[min_index], arr[i]

#testing
class TestSelectionSort(unittest.TestCase):

    def test_random_array(self):
        # Test 1: Randomly generated array
        arr1 = [random.randint(1, 100) for _ in range(10)]
        sorted_arr = sorted(arr1)
        selection_sort(arr1)
        self.assertEqual(arr1, sorted_arr)

    def test_sorted_array(self):
        # Test 2: Array already sorted in ascending order
        arr2 = [5, 15, 25, 35, 45, 55]
        selection_sort(arr2)
        self.assertEqual(arr2, [5, 15, 25, 35, 45, 55])

    def test_descending_array(self):
        # Test 3: Array sorted in decending order
        arr3 = [55, 45, 35, 25, 15, 5]
        selection_sort(arr3)
        self.assertEqual(arr3, [5, 15, 25, 35, 45, 55])

    def test_same_elements_array(self):
        # Test 4: Array with all the same elements
        arr4 = [5, 5, 5, 5, 5, 5]
        selection_sort(arr4)
        self.assertEqual(arr4, [5, 5, 5, 5, 5, 5])

    def test_empty_array(self):
        # Test 5: Empty array
        arr5 = []
        selection_sort(arr5)
        self.assertEqual(arr5, [])

    def test_single_element_array(self):
        # Test 6: Array with one element
        arr6 = [58]
        selection_sort(arr6)
        self.assertEqual(arr6, [58])


if __name__ == '__main__':
    unittest.main()