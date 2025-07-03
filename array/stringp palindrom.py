print("write a palindrome word ")

word=input("enter the word:")

if word==word[::-1]:
    print('the word is a palindrom')
else:
    print('word is not a palindrom')


