<!--
Problem 2: Search in a Rotated Sorted Array

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

# Problem 2

## Reasoning Behind Decisions

The **`rotated_array_search`** function is designed to efficiently find a target element in a **rotated sorted array** using **binary search**. The key design choices include:

1. **Binary Search Approach**:  
   - Binary search enables an optimal solution by continuously dividing the search space in half  
   with a time complexity of ${O(\log\ n)}$.

2. **Handling Rotated Sorted Arrays**:  
   - A rotated sorted array has two sorted halves.
   - The algorithm determines whether the **left half** or **right half** is sorted.
   - If the left half is sorted and contains the target, the function searches in the left half; otherwise in the right half.
   - If the right half is sorted and contains the target, the function searches in the right half; otherwise in the left half.

3. **Handling Edge Cases**:  
   - The function returns ${-1}$ when the target number is not found.
   - The edge case of an empty list return ${-1}$ as well.

This approach ensures efficient searching with a logarithmic time complexity while correctly handling rotated arrays.

## Time Efficiency

The function achieves an ${O(\log\ n)}$ time complexity due to the binary search approach:

1. **Binary Search Iteration**:
   - At each step, the search range is reduced by half.
   - This results in at most ${\log\ n}$ iterations.

2. **Constant-time Operations**:
   - Computing the midpoint and performing comparisons all run in ${O(1)}$ time.

Thus, the overall time complexity is ${O(\log\ n)}$.

## Space Efficiency

The function operates with ${O(1)}$ space complexity:

1. **Constant Extra Space**:
   - Only a few integer variables (${left}$, ${right}$, ${mid}$) are used.
   - No additional data structures (*arrays*, *recursion stacks*) are needed.

2. **In-Place Computation**:
   - The function modifies variables directly within the loop, avoiding extra memory allocations.

Thus, the function achieves optimal space efficiency while maintaining fast execution.
