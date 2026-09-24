''' 1. Write a Python program that calculates the factorial of a given number n (n!) using both a for loop
and a while loop.

num1=int(input("Enter a number:"))
fact=1
for i in range(1,num1+1):
    fact=fact*i
    if i<num1:
        print(i, end=" X ")
    else:
        print(i, end=" ")
print("\nFactorial of number: ",num1, ", is :", fact)

2. Write a Python program that finds and prints all the prime numbers between 1 and N using both a
for loop and a while loop.
from operator import truediv

N=int(input("Enter a number:"))
for i in range(1,N+1):
    prime = True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        print("Prime no.: ", i, end=" ")

3. Write a Python program that counts the number of digits in a given number using both a for loop
and a while loop.
#from itertools import count
count=0
N=int(input("Enter a number:"))
for i in str(abs(N)):
    if N>0:
        count+=1
print("No. of digits count :", count)
print(type(str(abs(N))))


# using while loop
N=int(input("Enter a number:"))
count=0
if N==0:
    count=1
else:
    while N!=0:
        N=N//10
        count+=1
print("No. of digits count :", count)

4. Write a Python program that calculates the sum of the first N natural numbers (1 + 2 + 3 + ... + N)
using both a for loop and a while loop.

N=int(input("Enter a number: how much first natural no. sum u required :"))
sum=0
for i in range(1,N+1):
    sum+=i
print("the sum of the first N natural numbers :", sum)

5. Write a Python program that generates the Fibonacci series up to N terms using both a for
loop and a while loop.'''

N=int(input("Enter a number for Fibonacci series:"))
n1=0
n2=1
print("Fibonacci series upto ",N," terms:")
'''for i in range(1,N+1):
    print(n1,end=" ")
    n3=n1+n2
    n1=n2
    n2=n3'''
i=1
while i<=N:
    print(n1,end=" ")
    n3=n1+n2
    n1=n2
    n2=n3
    i=i+1












