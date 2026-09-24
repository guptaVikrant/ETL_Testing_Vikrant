#input
'''
name=input("Enter your name:")
print("Your name is: ",name)
print("Data type of name is: ",type(name))

age=int(input("Enter your age:"))
print("Your age is: ",age)
print("Data type of age is: ",type(age))

from asyncio import constants a=5
a=10
b=20
a=a+b
print(a)
a="Vikrant"
b="Gupta"
a=a+" "+b
print(a)

# Control statement
age=int(input("Enter your age:"))

if age>18:
    print("You are eligible for vote")
elif age==18:
    print("You are near to eligible for vote")
else:
    print("You are not eligible for vote")


# Looping statement
# For loop
for num in range(20):
    print(num)
for num in range(2,21,3):
    print(num)


# while loop

start_val=1
end_val=10
while start_val<=end_val:
    print(start_val)
    start_val=start_val+1
print(end_val)

# Boolean
a=True
b=False
ans1= a and b
ans2= a or b
ans3= not a or b
print("a=True,b=False")
print("a and b: ",ans1)
print("a or b: ",ans2)
print("not a or b: ",ans3)
print(type(ans3))
'''

duration=int(input("Enter your duration:"))
if duration<=30:
    print("SLA Met")
elif duration<=45:
    print("SLA warning")
else:
    print("SLA breached")





# looping statement
