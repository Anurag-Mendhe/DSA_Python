What is Search ?
Search is a process of finding a specific item or value within a collection of iterms or data
It locates a particular element in a dataset for retrieval, update, or decision making

Types of Search
-------------------------------------------------------------------------------------------------------------------------------------
1. Linear Search
A straightforward approach where each element in the list is checked sequentially untill the target is found or the list ends
Time Complexity : O(n)
Example : Checking the book on a shelf by checking each book one by one.

2. Binary Search
Binary Search is a divide-and-conquer algorithm used to find the position of a target element in a sorted array.
Instead of checking each element one by one (like Linear Search), it repeatedly divides the search interval in half, making it much faster.
Time Complexity : O(log n)
Example : Looking for a word in a dictionary by opening it to the middle and determining which half to search next.
-------------------------------------------------------------------------------------------------------------------------------------
Binary Search Algorithm:
1. Initialization : Start with two pointers (low and high)
2. Midpoint Calculation : Find the middle element (mid)
3. Comparison : Compare the middle element with the target
4. Narrowing Down : Update / Adjust the search range based on the comparison
-------------------------------------------------------------------------------------------------------------------------------------

🔹 How it Works

Start: With the entire array.
Set low = 0, high = n-1.
Find mid: mid = (low + high) // 2.
Compare:
If arr[mid] == target → found! return index.
If arr[mid] < target → search in the right half (low = mid + 1).
If arr[mid] > target → search in the left half (high = mid - 1).
Repeat steps 2–3 until low > high (target not found).

🔹 Example

Array: [3, 4, 7, 8, 10, 32, 67]
Target: 10

Step 1: low=0, high=6, mid=3 → arr[3]=8 → 10 > 8 → search right half
Step 2: low=4, high=6, mid=5 → arr[5]=32 → 10 < 32 → search left half
Step 3: low=4, high=4, mid=4 → arr[4]=10 → found at index 4 ✅

🔹 Time Complexity

Each step halves the search range.
Worst case, it takes log₂(n) steps.
Best Case	O(1) (target found at mid on first try)
Average	O(log n)

🔹 Space Complexity

Iterative version: O(1) (uses only a few variables).
Recursive version: O(log n) (due to recursion stack).

🔹 Binary Search vs Linear Search
Feature	                 Linear Search	          Binary Search
Input type	             Unsorted OK              Must be sorted
Best Case	               O(1)	                    O(1)
Worst Case	             O(n)	                    O(log n)
Space Complexity	       O(1)	                    O(1) iterative
Speed on large data	     Slow	                    Very fast

🔹 Binary Search with Sorted and Unsorted Array

Binary Search works by comparing the target with the middle element and deciding whether to go left or right.

🔹 Why Sorting is Required

Binary Search depends on ordering:
Everything to the left of mid is smaller.
Everything to the right of mid is larger.
Without sorting, this property doesn’t hold → Binary Search can discard the half where the answer actually exists.

If array is sorted:
arr[mid] < target → target must be on the right side.
arr[mid] > target → target must be on the left side.
This only makes sense if the array is in sorted order.

🔹 Example with Sorted Array
Array: [3, 4, 7, 8, 10, 32, 67]
Target = 10
mid = 8 → 10 > 8 → go right → ✅ 10 is actually in the right half.
Binary Search works perfectly.

🔹 Example with Unsorted Array
Array: [4, 8, 32, 67, 7, 3, 10]
Target = 10
low=0, high=6, mid=3 → arr[mid] = 67
10 < 67 → Binary Search will look left side [4, 8, 32].
But 10 is actually in the right side [7, 3, 10].
❌ Binary Search fails because the assumption about "left < mid < right" is broken in unsorted arrays.
  
✅ Summary:
Binary Search is one of the most efficient searching algorithms for sorted data, reducing time complexity from O(n) → O(log n).
