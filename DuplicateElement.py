li=[1,2,1,3,4,2,1,4]
duplicate=[]
for i in li:
    if i not in duplicate:
        duplicate.append(i)
print(duplicate)
