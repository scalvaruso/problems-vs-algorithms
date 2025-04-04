"""
Problem 3: Rearrange Array Elements

Given an input array consisting on only 0, 1, and 2, sort the array in a single 
traversal. You're not allowed to use any sorting function that Python provides.

Note that O(n) does not necessarily mean single-traversal. For e.g. if you 
traverse the array twice, that would still be an O(n) solution but it will not 
count as single traversal.

You should implement the function body according to the sort_012 function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

def sort_012(input_list: list[int]) -> list[int]:
    """
    Sort an array consisting only of 0s, 1s, and 2s in a single traversal.

    This function uses the Dutch National Flag algorithm to sort the array in-place.

    Args:
    input_list (list[int]): A list of integers where each integer is either 0, 1, or 2.

    Returns:
    list[int]: The sorted list with all 0s, followed by all 1s, and then all 2s.
    """
    if input_list is None:
        return []

    # Pointers for the next positions of 0, current, and 2
    left = 0                        # Next position for 0
    current = 0                     # Current element being checked
    right = len(input_list) - 1     # Next position for 2

    while current <= right:
        if input_list[current] == 0:
            # Swap 0 to the left
            input_list[left], input_list[current] = input_list[current], input_list[left]
            left += 1
            current += 1
        elif input_list[current] == 1:
            # 1 stays in the middle
            current += 1
        else:
            # Swap 2 to the right
            input_list[current], input_list[right] = input_list[right], input_list[current]
            right -= 1

    return input_list


def test_function(test_case: list[list[int]]) -> None:
    """
    Test the sort_012 function with a given test case.

    Args:
    test_case (list[list[int]]): A list containing one element:
        - A list of integers where each integer is either 0, 1, or 2, 
          representing the input array to be sorted.

    Returns:
    None: Prints the sorted array and "Pass" if the output from sort_012 
    matches the sorted input array, otherwise prints "Fail".
    """
    sorted_array: list[int] = sort_012(test_case[0])
    print(sorted_array)
    if sorted_array == sorted(test_case[0]):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    # Edge case: Empty input list
    test_function([[]])
    # Expected output: Pass

    # Normal case: Mixed elements
    test_function([[0, 1, 2, 0, 1, 2]])
    # Expected output: Pass

    # Normal case: Already sorted list
    test_function([[0, 0, 1, 1, 2, 2]])
    # Expected output: Pass

    # Normal case: Reverse sorted list
    test_function([[2, 2, 1, 1, 0, 0]])
    # Expected output: Pass

    # Edge case: None input (interpreted as empty list)
    test_function([[None]])
    # Expected output: Pass (Note: interpreted as a list with None, not a None input)

    # Edge case: Single element
    test_function([[1]])
    # Expected output: Pass

    # Edge case: All elements the same
    test_function([[0, 0, 0, 0]])
    test_function([[1, 1, 1]])
    test_function([[2, 2, 2, 2, 2, 2]])
    # Expected output: Pass for all

    # Edge case: Very large input
    test_function([[0, 1, 2] * 10000])  # 30,000 elements
    # Expected output: Pass
