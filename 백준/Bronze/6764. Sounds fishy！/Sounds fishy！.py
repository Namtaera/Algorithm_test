lists = []
for a in range(4):
    inputs = int(input())
    lists.append(inputs)

if lists[0] < lists[1] and lists[1] < lists[2] and lists[2] < lists[3]:
    print("Fish Rising")

elif lists[0] > lists[1] and lists[1]>lists[2] and lists[2] > lists[3]:
    print("Fish Diving")

elif lists[0] == lists[1] and lists[1] == lists[2] and lists[2] == lists[3] :
    print("Fish At Constant Depth")

else :
    print('No Fish')

