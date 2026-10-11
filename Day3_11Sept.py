# Primitive Data Type - int, float, string, boolean
# Non-primitive Data Type - Collection Data Type - list, tuple, set, dictionary

# List

name_lst=["Ram", "Shyam", "Ghanshyam", 30, 44,15]
'''print("name_list :",name_lst, " Type of List :",type(name_lst))
print("Index of Ghanshyam :",name_lst.index("Ghanshyam"))
name_lst.remove("Shyam")
print("name_list after removing Shyam:",name_lst)
name_lst.insert(0,"HareRam")
print("name_list after adding HareRam at [0] :",name_lst)
name_lst.append(50)
print("name_list after append 50 :",name_lst)
print ("length of len_lst=",len(name_lst))
name_lst.reverse()
print("name_list after reverse :",name_lst)
name_lst.sort()
print("name_list after sort :",name_lst)
'''

# tuple
name_tpl=("Ram", "Shyam", "Ghanshyam", 30, 44, "Shyam", 15)

name_lst.insert(3, "Shyam")
name_lst.append("Shyam")
'''
print(f"We have tuple {name_tpl} and type of tuple {type(name_tpl)}")
print(name_tpl[:5:2])
'''
# Set
name_set={"Ram", "Shyam", "Ghanshyam", 30, 44,15}

print("name_set :",name_set)
name_set.remove("Shyam")
print(f"name_set after removing Shyam : {name_set} and type is : {type(name_set)}")
name_set.add("HareRam")
print(f"name_set after adding HareRam : {name_set}")
'''
# Importent concept
a=[1,2]
b=a
print(a)
a.append(3)
print(b)

x=range(10)
print(list(x))
print(name_lst[2:])
print(len(name_lst))
print(len(name_tpl))

print(f" Check count of shyam in list {name_lst.count("Shyam")}")
print(f" Check index of ghanshyam in tuple {name_tpl.index("Ghanshyam")}")
print(f" Check index of 30 in list {name_lst.index(30)}")
print(name_lst)'''
print(len(name_set))

num1={1,2,3,4,6}
print(num1)
num2={2,4,6,8,10}
print(num2)
num3=num1|num2
mum4=num1.union(num2)
print(f"Union of num1 {num1} and num2 {num2} is num3 {num3} and num4 {mum4}")

num9=num1^num2
mum10=num1.symmetric_difference(num2)
print(f"Systematic difference of num1 {num1} and num2 {num2} is num9 {num9} and num10 {mum10}")

num5=num1&num2
mum6=num1.intersection(num2)
print(f"intersection of num1 {num1} and num2 {num2} is num5 {num5} and num6 {mum6}")
num7=num1-num2
mum8=num1.difference(num2)
print(f"Minus of num1 {num1} and num2 {num2} is num7 {num7} and num8 {mum8}")

for item in name_set:
    print(f"item of set {item} and data type of this item is {type(item)}")