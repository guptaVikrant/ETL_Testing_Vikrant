# a=> 97, z=>122, A=>65, Z=> 90

print(ord("Z"))
print(ord("a"))
print(ord("A"))

print(chr(68))
print(chr(65))

# Get the sum of ASCII value of characters in String
str1="International"
print(str1)
sum=0
for ch in str1:
    sum=sum+ord(ch)
print(sum)

# Count the occurrence of each number in  list using dictionary

def count_num_occurences(lst1)  :
    count_element={}

    for num in lst1 :
        if num in count_element :
            count_element[num]+=1
        else:
            count_element[num]=1
    return count_element


# Get all the duplicate no. direct using list

def dup_item_list(lst1):
    dup_lst = []
    for num in lst_num:
        if lst_num.count(num)>1 and num not in dup_lst :
            dup_lst.append(num)
    return dup_lst

def dup_item_dict(count_dict):
    dup_list = []
    for key in count_dict.keys() :
        if count_dict[key]>1 :
            dup_list.append(key)
    return dup_list

lst_num=[1,2,3,4,5,2,3,5,3]
print(f"item of list with occurrence : {count_num_occurences(lst_num)}")
print(f"Duplicate items from dictionary are : {dup_item_dict(count_num_occurences(lst_num))}")
print(f"Duplicate items direct list count are : {dup_item_list(lst_num)}")


