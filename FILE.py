chain=input("Enter a string : ")
chain_inverse=chain[::-1]
if chain==chain_inverse:
    print('the string is palindrome.')
else:
    print("the string is not palindrome.")