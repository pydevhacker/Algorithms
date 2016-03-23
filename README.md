<h1>Algorithms<h1>
<h2>Array</h2>
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

