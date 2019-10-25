list = [3,1,9,2,9]
print ("Original list: " , list)
changed = True

while changed:
    print("New Loop!")
    changed = False
    for i in range(0,len(list) - 1):
        print(list)
        if list[i] > list[i+1]:
            (list[i+1], list[i]) = (list[i], list[i+1])
            changed = True
