n = input()
lists = n[1:-1]


if (n[0]=='"' and n[-1]=='"') :
    if (len(lists) == 0) :
        print("CE")

    else :
        print(n[1:-1])

elif (n[1:-1] == "") :
    print("CE")

else :
    print("CE")
