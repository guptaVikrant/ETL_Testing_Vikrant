'''Write a function to return a list of all prime numbers between to 2 to N where N is the
number that the function receives as an input.
'''
def findPrimeList(N):
    primeList=[]
    prime1=False
    for i in range(2,N+1):
        for j in range(2,i):
            if i%j!=0:
                prime1=True
            else:
                prime1=False
                break
        if prime1==True:
            primeList.append(i)
    return primeList

N=int(input("Enter a number: "))
prm_lst=findPrimeList(N)
print(prm_lst)

# 2. Write a function to return a list with all the duplicate elements from the list
# 3. Write a function to return a list with all the unique elements from the list

def dupList(lst):
    count=0
    temp_lst=[]
    single_lst=[]
    dup_lst=set()
    for item in lst:
        if item not in temp_lst:
            count=1
            temp_lst.append(item)
        else:
            count+=1
            dup_lst.add(item)
        if lst.count(item)==1:
            single_lst.append(item)
    return dup_lst,single_lst

new_lst=[11, 55, 66, "Shyam", 33, "RAM", 15, "RAM", 23, 12, "RAM", 23, 11, "Bharat", 15, 'a', 12, 'a', 'b', 55, 'a']
print(new_lst)
print(f"Duplicate items and Unique items : {dupList(new_lst)}")

from enum import unique


# 4. Write a Python program to find the sum of all elements in the list and print.
# 5. Write a program to find the largest number in the list and return.
# 7. Find the Second Largest Element and print
def lstsum(lst):
    sum=0
    for item in lst:
        sum+=item
    return sum
def  nummax(lst):
    max1=lst[0]
    for item in lst:
        if item > max1:
            max1=item
    return max1

def secondMax(lst):
    max2=lst[0]
    max1=0
    temp=0
    for item in lst:
        if item > max1:
            max2=max1
            max1=item
        elif item > max2 and item != max1:
            max2=item
    return max2

num_lst=[4, 2, 9, 55, 33, 22, 81, 67, 25, 3]
total=lstsum(num_lst)
max_num=nummax(num_lst)
sec_max=secondMax(num_lst)
print(f"Total of all items in the list: {num_lst} is {total}")
print(f"Max number is: {max_num} and second max number is: {sec_max}")

# 6. Remove Duplicates from a List and return the list

def dupRemoveList(lst):
    count=0
    temp_lst=[]
    dup_lst=set()
    for item in lst:
        if item not in temp_lst:
            count=1
            temp_lst.append(item)
        else:
            count+=1
            dup_lst.add(item)
    print(f"List of duplicates : {dup_lst}")
    return temp_lst

new_lst=[11, 55, 66, "Shyam", 33, "RAM", 15, "RAM", 23, 12, "RAM", 23, 11, "Bharat", 15, 'a', 12, 'a', 'b', 55, 'a']
print(f"List before removal duplicate : {new_lst}")
new1=dupRemoveList(new_lst)
print(f"List after removing duplicates : {new1}")
set(new_lst)
print(f"List after removing duplicates : {set(new_lst)}")
copy_lst=new_lst[:]
print(f"List after copy from new list : {copy_lst}")

