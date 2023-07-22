#progaram to remove vowel from a word
a=str(input("enter your word:"))
vowels=("a","e","i","o","u","A","E","I","O","U")
for i in a:
    if i in vowels:
        a=a.replace(i,"")
print(a)
