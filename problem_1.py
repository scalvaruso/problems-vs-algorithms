"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored square root

    Returns:
    int: Floored square root
    """

    # Handle negative numbers, as their real square root is undefined.

    if number < 0:
        return None                 # Returning None to indicate invalid input.

    # Handle base cases: sqrt(0) = 0, sqrt(1) = 1.

    if number == 0 or number == 1:
        return number

    # Using binary search to find the floored square root efficiently.
    # Binary search runs in O(log n) time complexity.

    left, right = 1, number         # Search space: from 1 to number.
    solution = 0                    # Variable to store the potential answer.

    while left <= right:
        mid = (left + right) // 2   # Find the middle element.
        mid_squared = mid * mid     # Compute mid squared.

        if mid_squared == number:
            return mid              # If mid^2 is exactly the number, return mid.
        elif mid_squared < number:
            solution = mid          # Store mid as a potential floor value.
            left = mid + 1          # Search the right half for a larger value.
        else:
            right = mid - 1         # Search the left half for a smaller value.

    return solution                 # Return the floor value of sqrt(number).


if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
    print("Pass" if 37 == sqrt(1432) else "Fail")  # Expected Output: Pass
    print("Pass" if None == sqrt(-2) else "Fail")  # Expected Output: Pass
