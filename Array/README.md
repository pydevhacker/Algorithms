# Array



<h3> Problem 5 : 
<a href='http://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/'>
Generate all possible sorted arrays from alternate elements of two given sorted arrays</a> </h3>

<b>Solution</b> : `Array/Problem5.py`

<p>Given two sorted arrays A and B, 
generate all possible arrays such that first element is taken 
from A then from B then from A and so on in increasing order till the arrays exhausted. 
The generated arrays should end with an element from B.
</p>
<pre>
For Example 
A = {10, 15, 25}
B = {1, 5, 20, 30}

The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30
</pre>

<h2><b>Problem 6 : </b><a href='http://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/'>
Smallest subarray with sum greater than a given value</a></h2>
<b>Solution</b> : `Array/Problem6.py`

<br/>

<pre>
Given an array of integers and a number x, find the smallest subarray with sum greater than the given value

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}
</pre>

>This is line one