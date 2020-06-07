"""
Consecutive Prime Sum

Some prime numbers can be expressed as a sum of other consecutive prime numbers. 
For example 
5 = 2 + 3, 
17 = 2 + 3 + 5 + 7, 
41 = 2 + 3 + 5 + 7 + 11 + 13. 
Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.

Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.


Input Format: First line contains a number N

Output Format: Print the total number of all such prime numbers which are less than or equal to N.

Constraints: 2<N<=12,000,000,000
"""

n=int(input("Enter the number : "))

def isprime(n):
    res=True
    for i in range(2,(n//2)+1):
        if(n%i==0):
            res=False
            break
    return res

arr=[]

for i in range(2,n):
    if(isprime(i)):
        arr.append(i)

sum=0
count=0
for i in arr:
    sum+=i
    if(isprime(sum) and sum<=n):
        count+=1


print(count-1)
