#1. Write a function to return the grade based on percentage
'''
def grade(m):
    if m>=90:
        return "A"
    elif m>=80:
        return "B"
    elif m>=70:
        return "C"
    elif m>=60:
        return "D"
    else:
        return "F"

marks=int(input("Enter marks:"))
print(f"Grade of student is : {grade(marks)}")


#2. Write a function that return a list of common elements from two different sets.
def commonOfSets(set1, set2):
    #set1.sort()
    #set2.sort()
    common_lst=[]
    for item in set1:
        if item in set2:
            common_lst.append(item)
    return common_lst

s1={7, "RAM", 18, "SHYAM", 36, 12, "HARERAM"}
s2={"SHYAM", 1, 2, 7, 10, 12, "Hari", "RAM"}
new_lst=commonOfSets(s1,s2)
print(f"Common list from both sets is: {new_lst}")

#3. Convert a String to a List of Characters

def listChr(name):
    name_cr=[]
    name_cr=list(name)
    return name_cr
   #for i in name:
   #name_cr.append(i)

usr_name=input("Enter your name:")
lst_nm_chr=listChr(usr_name)
print(f"List od characters from {usr_name} is {lst_nm_chr}")

#4. Write a function to check if list contains any duplicate element and return True or False as
#applicable
def duplicates(lst):
    temp_lst=[]
    dup_lst=[]
    chk=False
    for i in lst:
        if i not in temp_lst:
            temp_lst.append(i)
        else:
            dup_lst.append(i)
            chk=True

    return chk, dup_lst

new_lst=["Ram", "Shyam", "Ghanshyam", 30, 44, "Ram", 12, 30, "Ram", 30, 15]
print(f"Check if list contains any duplicate element in {new_lst} : {duplicates(new_lst)}")


#5. Given a list, write a function that provide the occurrence of element against each element
# in the list. e.g. List = [1,2,3,4,5,1,3]

lst1 = [1, 2, 3, 1, 4, 5, 3, 1, 3, 2, 5, 1]
temp=[]
#count=0
for i in range(len(lst1)):
    if lst1[i] not in temp:
        count = 0
        for j in range(len(lst1)):
            if lst1[i]==lst1[j]:
                count=count+1
        print(f"occurrence of item {lst1[i]} is : {count}")
        temp.append(lst1[i])


Write a function return a substring where it starts from 2rd occurrence of ‘a’ and end at
occurrent of ‘b’
e.g. s = "abracadabra"
start_char = 'a'
end_char = 'b'
Expected output: acadab
'''

def subStrNew(str1,start_char,end_char):
    count=0
    start=-1
    end=-1

    for i in range(len(str1)):
        if str1[i] == start_char:
            count+=1
            if count==2:
                start=i
    #for j in range(start+1,len(str1)):
        if str1[i] == end_char and start !=-1:
            end=i
            break
    if start!=-1 and end!=-1:
        for k in range(start,end+1):
             print(str1[k],end="")


str1="abracadabra"
start_char='a'
end_char='b'
print(f"Sub String of {str1} start with {start_char} and end with {end_char} is :")
subStrNew(str1,start_char,end_char)
