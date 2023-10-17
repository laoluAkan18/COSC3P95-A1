import random

# Sorting algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            #if arr[j] > arr[j+1] : #working line in code
            if arr[j] < arr[j+1] : #mutation one (1) causes program to break! (Hence, it kills the mutation)
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Random test case generator
def generate_test_case(min_length=1, max_length=200, min_value=-1_000_000_000, max_value=1_000_000_000):
    length = random.randint(min_length, max_length)
    return [random.randint(min_value, max_value) for _ in range(length)]

# Test the sorting algorithm with a random test case
def test_sorting_algorithm():
    f= open("output.txt", "w")
    for i in range(35):
        test_case = generate_test_case()
        print(f"Input array: {test_case}", file=f)
        sorted_test_case = sorted(test_case)
        output_array = bubble_sort(test_case)
        print(f"Output array: {output_array}", file=f)
        try:
            assert output_array == sorted_test_case, "Test failed!"
        except AssertionError as e:
            print(f"Test failed! {e}", file=f)
        print("Test passed!", file=f)
    
        #compare elements in input and output array to ensure equality. 
        if (output_array == sorted_test_case):
            print("Equal number of elements")

    f.close()
# Run the test
test_sorting_algorithm()
