'''1. Given a string , write a python code to reverse the string using for loop and slice operator both
ways?
Input: city = "ETLQALabs"
expected output: “sbaL AQ LTE”
str1=input("Enter the string :")
#using for loop
for i in range(len(str1)-1,-1,-1):
   print(str1[i],end="")
print()
# using slicer
str2=str1[len(str1)-1::-1]
print("Reverse string using slicer:", str2)
 2. Extract a substring form character "Q" and ends at "b"
Input: city = "ETLQALabs"
Expected O/P : QAlab
strt_indx=str1.index('Q')
end_indx=str1.index('b')
str3=str1[strt_indx:end_indx+1:]
print(str3)

4 & 5.How would you use slicing to create a new list containing only the odd-indexed elements of a
given list?
Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected output : [1, 3, 5, 7, 9]

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_odd_indx=list1[1::2]
list_even_indx=list1[0::2]
print(list_odd_indx)

print(f"Odd index elements from list: {list1} is showing in list 2 {list_odd_indx}")
print(f"even index elements from list: {list1} is showing in list 2 {list_even_indx}")

 3. Write a python code to check if the given list contains duplicate elements and print yes or no as
per input
e.g.
list1 =[1,2,3,4,3] => Yes
list2 =[1,2,3,4] => No'''

list1 =[1, 2, 3, 4, 3]
dup=False
for item in set(list1):
    if list1.count(item) > 1:
        dup=True
        break

'''
temp=[]
count=0
dup=False
for i in range(len(list1)):
    if list1[i] not in temp:
        temp.append(list1[i])
    else:
        dup=True
        break
       
print(f"Check whether we have duplicate ite : {dup}")

 '''
new_string=input("Enter the new string :")
new_lst=[]
for i in new_string:
    new_lst.append(i)
for j in set(new_lst):
    print(f"count of each character is : count of {j} is : {new_lst.count(j)}")




