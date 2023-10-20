##
# COSC 3P95 Assignment One (1) Question six (6)
#
# Name: Olaoluwa Akanji
# Student Number: 6908776
# Brock UserName: la19xl
#
# Description: This class presents a Python program that implements a basic delta debugging tool for minimizing testcases.
#

#bugged code
def processString(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char * 2
        else:
            output_str += char.upper()

    return output_str 

#expectations: fixed code
def expected_output(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        elif char.isnumeric():
            output_str += char
        else:
            output_str += char.upper()

    return output_str 

#minimizing algorithm
def delta_debug(input_str):
    # If the entire string does not fail the test, return None
    if not test_func(input_str):
        return None

    n = 2  # Initial granularity
    while len(input_str) >= n:
        subset_length = len(input_str) // n
        i = 0
        while i < len(input_str):
            subset = input_str[i:i+subset_length]
            if test_func(subset):  # If the bug appears in the subset
                input_str = subset  # Reduce the input size
                n = max(n - 1, 2)  # Try a smaller granularity
                break
            i += subset_length
        else:
            if n == len(input_str):
                break  # Cannot reduce further
            n = min(n * 2, len(input_str))  # Increase granularity
    return input_str

#tester function
def test_func(input_str):
    return processString(input_str) != expected_output(input_str)

# Test delta_debug with given test cases.
print(delta_debug("abcdefG1"))
print(delta_debug("CCDDEExy"))
print(delta_debug("1234567b"))
print(delta_debug("8665"))
