#Dictionary
'''
emp_det={1:"Vikky", 2:"Raju", 3:"Sonu"}
print(f"Complete dictionary is as follows: {emp_det}")
for i in emp_det:
    print(f"Value {i} from dictionary are as : {emp_det[i]}")

stud_det={"rollNo":101, "Name":"Vikky", "Age":35, "Profession":"QA"}
print(f"Complete Student detail: {stud_det} and type of detail {type(stud_det)}")
stud_det["Salary"]=200000
print(f"Updated Student detail: {stud_det}")
# Removing based on key.
stud_det.pop("Age")
print(f"Updated Student detail: {stud_det}")
stud_det["Age"]=28
print(f"Updated Student detail: {stud_det}")
rem_value=stud_det.pop("Profession")
print(f"Updated Student detail after removing {rem_value} : {stud_det}")

# Removing based on last item.
rem_item=stud_det.popitem()
print(f"Updated Student detail after removing {rem_item} : {stud_det}")

#Iteration based on key
for key in stud_det.keys():
    print(f"{key} ")

#iteration based on values
for value in stud_det.values():
    print(value)


#Iteration based on key value pair
for key, value in stud_det.items():
    print(f"{key} : {value}")

#Access key and value separate
for item in stud_det.items():
    print(f"{item[0]} : {item[1]}")
    
'''

num_lst=[4, 2, 9, 55, 33, 22, 81, 67, 25, 3]
print(f"List oiginal :{num_lst}")
print(f"Highest number is {sorted(set(num_lst))[-1]} and Second max number from list is :{sorted(set(num_lst))[-2]}")
'''num_lst.sort()
print(num_lst)
num_lst.reverse()
print(num_lst[-2])'''