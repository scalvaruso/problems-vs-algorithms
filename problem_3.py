"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""


"""
NOTE To run the last test the folder "data/" with the additional files
needs to be copied in the same folder of problem_3.py
"""


def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """
    # Edge case: Empty list
    if not input_list:
        return (0, 0)

    # Step 1: Sort the list in descending order based on absolute values
    sorted_list = merge_sort_desc(input_list)

    # Step 2: Distribute numbers into two separate lists
    num1_list, num2_list = [], []
    
    for i, num in enumerate(sorted_list):
        if i % 2 == 0:
            num1_list.append(num)  # Even indices go to num1
        else:
            num2_list.append(num)  # Odd indices go to num2
    
    # Step 3: Convert the lists of digits into integers
    def list_to_number(num_list):
        """
        Converts a list of single-digit numbers into an integer while 
        maintaining correct sign placement.

        Args:
        num_list (list[int]): List of single-digit numbers.

        Returns:
        int: The constructed integer.
        """
        if not num_list:  # If the list is empty, return 0
            return 0
        
        # Convert absolute values to string and concatenate
        num_str = "".join(str(abs(digit)) for digit in num_list)
        
        # Convert to integer, applying sign from the first element
        return int(num_str) if num_list[0] >= 0 else -int(num_str)

    num1 = list_to_number(num1_list)
    num2 = list_to_number(num2_list)

    return (num1, num2)


def merge_sort_desc(arr: list[int]) -> list[int]:
    """
    Perform merge sort in descending order based on absolute values.
    
    This function recursively divides the input array into halves,
    sorts them separately, and then merges them back in descending order.
    
    Args:
    arr (list[int]): The input list of numbers.
    
    Returns:
    list[int]: A new list sorted in descending order based on absolute values.
    """
    if len(arr) <= 1:
        return arr  # Base case: A list of 0 or 1 elements is already sorted.
    
    mid = len(arr) // 2  # Find the middle index
    left = merge_sort_desc(arr[:mid])  # Recursively sort the left half
    right = merge_sort_desc(arr[mid:])  # Recursively sort the right half
    
    return merge_desc(left, right)  # Merge the two sorted halves


def merge_desc(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists into a single list sorted in descending order 
    based on absolute values.
    
    Args:
    left (list[int]): The first sorted list.
    right (list[int]): The second sorted list.
    
    Returns:
    list[int]: A merged list sorted in descending order.
    """
    merged = []
    i, j = 0, 0  # Initialize pointers for both halves
    
    # Merge elements in descending order based on absolute value
    while i < len(left) and j < len(right):
        if abs(left[i]) >= abs(right[j]):  # Compare absolute values
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged


def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == '__main__':
    
    # Normal case: List of positive numbers
    test_function(([5, 1, 4, 9, 7, 2, 3, 8, 0, 6], [97531, 86420]))
    # Expected output: Pass

    # Normal case: List of negative numbers
    test_function(([-5, -1, -4, -7, -2, -3, -8, -6], [-8642, -7531]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [531, -42]))
    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with ones and zeros
    test_function(([0, 1, 0, 1, 0], [100, 10]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    """ 
    NOTE
    Since in the problem instruction is stated that:
    "The number of digits in both the numbers cannot differ by more than 1."
    The tuple used to obtain "Pass" in the test should be:
    ([2, 2, 2, 2, 2], [222, 22])
    not
    ([2, 2, 2, 2, 2], [222, 2])
    """
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Expected output: Pass

    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Edge case: Empty list
    test_function(([], [0, 0]))
    # Expected output: Pass

    # Edge case: Very large list (8600 numbers)

    import ast  # Importing auxiliary library
    # Importing "input_list" and "solution" data from files
    with open("data/very_large_list.txt", "r") as file:
        vll_data = file.read()
        very_large_list = ast.literal_eval(vll_data)
    with open("data/very_large_solution.txt", "r") as file:
        vls_data = file.read()
        very_large_solution = ast.literal_eval(vls_data)

    test_function((very_large_list, very_large_solution))
    # Expected output: Pass