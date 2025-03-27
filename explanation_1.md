<!--
Problem 1: Square Root of an Integer

Provide an explanation for your answer, clearly organizing your thoughts into 
concise and easy-to-understand language.

Focus on explaining the reasoning behind your decisions rather than giving a 
detailed description of the code. For instance, why did you choose a particular 
data structure? Additionally, discuss the efficiency of your solution in terms 
of time and space complexity. If necessary, you can support your explanation 
with code snippets or mathematical formulas. For guidance on how to write 
formulas in markdown, refer to https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions.
-->

# Problem 1

## Reasoning Behind Decisions

The implementation of the **`sqrt`** function is designed to efficiently compute the floored square root of a given integer using **binary search**.
The key design choices include:

1. **Binary Search Approach**:  
   - Since a brute-force approach would take ${O(\sqrt{n})}$ time, a more optimal solution is required.
   - The binary search technique allows us to efficiently narrow down the range of possible square roots.
   - It reduces the problem size by half at each step, ensuring an optimal ${O(\log n)}$ runtime.

2. **Handling Edge Cases**:  
   - If the number is negative, we return ${None}$, as negative numbers do not have Real square roots.
   - If the number is ${0}$ or ${1}$, the function directly returns the number itself since $\sqrt{0} = 0$ and $\sqrt{1} = 1$.

3. **Binary Search Execution**:  
   - We start with a search range of ${[1, number]}$, iterating until ${left}$ exceeds ${right}$.
   - If $mid^2$ equals the number, we return ${mid}$.
   - If $mid^2$ is smaller than the number, we update ${solution}$ and search the right half.
   - Otherwise, we search the left half to find a smaller candidate.
   - The final ${solution}$ holds the largest integer whose square is ≤ ${number}$.

This approach ensures the function runs efficiently while handling various edge cases.

## Time Efficiency

The function achieves an ${O(\log n)}$ time complexity due to the binary search approach:

1. **Binary Search Iteration**:
   - At each step, the search range is divided in half.
   - This results in $\log n$ iterations, making it highly efficient.

2. **Comparison and Computation**:
   - Computing $mid\times{mid}$ and checking conditions all run in ${O(1)}$ time.

Thus, the overall time complexity is ${O(\log n)}$.

## Space Efficiency

The function operates with ${O(1)}$ space complexity:

1. **Constant Extra Space**:
   - Only a few integer variables (${left}$, ${right}$, ${mid}$, ${solution}$) are used.
   - No additional data structures (like *arrays* or *recursion stacks*) are required.

2. **In-Place Computation**:
   - The function modifies variables in place without requiring extra memory allocations.

Thus, the function achieves optimal space efficiency while maintaining fast execution.
