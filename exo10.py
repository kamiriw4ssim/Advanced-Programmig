


    
word = input("Please type in a word: ")
    
    
is_palindrome = True
    
    
for i in range(len(word) // 2):
        
    if word[i] != word[len(word)-i-1]:
        is_palindrome = False
        break  
    
    
if is_palindrome:
        print("Yes, it's a palindrome.")
else:
        print("No, it's not a palindrome.")


