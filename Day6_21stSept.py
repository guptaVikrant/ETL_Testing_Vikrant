# take out last 4 characters
from Assignment_5 import sentence

s="Bangalore"
start_x=len(s)-1
end_x=len(s)-4
print(s)
print("Print 4 last char in reverse order : ",s[start_x:end_x-1:-1])
print("Print 4 last char in reverse order : ",s[-1:-5:-1])
print("Print 4 last char in positive order : ",s[end_x:start_x+1:1])

S2="Bangalore City"
# Print reverse
print(S2[::-1])

Sentence="I am an expert in QA and channel name QA Solutions and Expert in Maths, also QA is my passion."
words=Sentence.split()
print("Reverse the order of the words :")
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")
print()
print("Reverse the order of the words without for loop using slicing :")
revList=words[::-1]
print("Reverse order of words in list : ",words[::-1])
ans=""
#for item in revList:
print("Reverse the order of the words without for loop using JOIN :")
print(" ".join(revList))

print(Sentence[::-1])
print("words without for loop using slicing :")
print(S2[:int(len(S2)/2):])


