import random 
##
# COSC 3P95 Assignment One (1)
#
# Name: Olaoluwa Akanji
# Student Number: 6908776
# Brock UserName: la19xl
#
# Description: This class presents a Python program that implements a basic bubble sort algorithm. Additionally, it implements a function for generating randomized test cases.
#

# Bubble-sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            #if arr[j] > arr[j+1] : #original, functional line of code.
            if arr[j] < arr[j+1] : #mutation: Alters the bubble sort algorithm to sort in descending order rather than ascending order.
                #The tester identifies and responds to this bug, effectively neutralizing the mutation.
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#This function serves as a test case generator, creating an array with random lengths falling within the range of min_length and max_length. 
#Each element within the array is assigned a random integer value, which lies within the bounds of min_value and max_value.
def generate_test_case(min_length=1, max_length=200, min_value=-1_000, max_value=1_000):
    length = random.randint(min_length, max_length)
    return [random.randint(min_value, max_value) for _ in range(length)]

#This function generates a random test case, applies the bubble sort algorithm to sort it, 
#and verifies if the resulting output matches the expected output (the array sorted using Python's built-in sorting method.)
def test_sorting_algorithm():
    f= open("output.txt", "w") # Open a file to write the output
    for i in range(35): # Run the test 35 times
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
    
        #compare elements in input and output array to ensure equality/consistency. 
        if (output_array == sorted_test_case):
            print("Equal number of elements")

    f.close() #close file

test_sorting_algorithm()