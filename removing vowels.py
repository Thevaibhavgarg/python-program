#progaram to remove vowel from a word
a=str(input("enter your word:"))
b=len(a)
c=str()
for i in range(b):
    if a[i].lower()!="a":
        if a[i].lower()!="e":
            if a[i].lower()!="i":
                if a[i].lower()!="o":
                    if a[i].lower()!="u":
                          c=c+a[i]
print("your word after removing vowel is:",c)
