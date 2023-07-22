#progaram to highliting vowel from a word
a=str(input("enter your word:"))
vowels=("a","e","i","o","u","A","E","I","O","U")
for i in a:
    if i in vowels:
        print("(",i,")",end="",sep="")
    else:
        print(i,end="",sep="")
