"""
Collecting Candies

Krishna loves candies a lot, so whenever he gets them, he stores them so that he can eat them later whenever he wants to.

He has recently received N boxes of candies each containing Ci candies where Ci represents the total number of candies in the ith box. Krishna wants to store them in a single box. The only constraint is that he can choose any two boxes and store their joint contents in an empty box only. Assume that there are infinite number of empty boxes available.

At a time he can pick up any two boxes for transferring and if both the boxes say contain X and Y number of candies respectively, then it takes him exactly X+Y seconds of time. As he is to eager to collect all of them he has approached you to tell him the minimum time in which all the candies can be collected.



Input Format:



The first line of input is the number of test case T
Each test case is comprised of two inputs
The first input of a test case is the number of boxes N
The second input is N integers delimited by whitespace denoting the number of candies in each box


Output Format: Print minimum time required, in seconds, for each of the test cases. Print each output on a new line.



Constraints:



1 ?T?10
1 ?N? 10000
1 ? [Candies in each box] ? 100009


Sample Input and Output:




1
4
1 2 3 4	

3,6,10

19


1
5
1 2 3 4	

34

"""
t=int(input("Enter the testcase : "))

for i in range(t):
    n=int(input("Enter the box size"))
    l=list(map(int,input("Enter the candies : ").split(" ")))
    l.sort()
    sec=[]
    count=l[0]
    for i in range(1,len(l)):
        count=count+l[i]
        sec.append(count)

print(sum(sec))
print(sec)

