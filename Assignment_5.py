# 1. Extract Username and Domain from Email
from collections import Counter

email="vikrantgupta.qa@gmail.com"
email_lst=email.split("@")
print(email_lst[1])

# 2. Count Words in a Sentence
Sentence="I am an expert in QA and channel name QA Solutions and Expert in Maths, also QA is my passion."
'''words_count=Counter(Sentence)
print(words_count) '''
words=Sentence.split()
word_count=len(words)
print(f"we have these words {words} in our sentence with {word_count} words")

# 5. Reverse the Order of Words
print("Reverse the order of the words :")
for i in range(word_count-1,-1,-1):
    print(words[i],end=" ")

# 3. Extract File Extension
# 4. Split CSV Data
# 6. Find Domain from Multiple Emails emails = ["ajay@gmail.com", "neha@yahoo.com", "ritu@outlook.com"]
# 7. Split a File Path path = "C:/Users/Ajay/Documents/file.txt"
# 8. Extract First and Last Name
# 9. Clean Multiple Spaces Between Words  sentence = "Python  is   very    easy"
# 10. Extract Top-Level Domain (TLD) Top-Level Domain: com

# 6. Find Domain from Multiple Emails emails = ["ajay@gmail.com", "neha@yahoo.com", "ritu@outlook.com"]
print()
print("Domain from Multiple Emails")
emails = ["ajay@gmail.com", "neha@yahoo.com", "ritu@outlook.com"]
for email in emails:
    email_lst=email.split("@")
    print(email_lst[1])

# 9. Clean Multiple Spaces Between Words  sentence = "Python  is   very    easy"
print()
print("Striped Sentence")
sentence = "Python  is   very    easy"
print(" ".join(sentence.split()))