n = int(input().strip())
s = input().strip()
k = int(input().strip()) % 26
l = list(s)
e = []
for item in l:
    z = ord(item)
    if (z >= 97 and z <= 122):
        if (z+k) > 122:
            e.append(chr(96 + (z+k-122)))
        else:
            e.append(chr(z+k))
    elif (z >= 65 and z <= 90):
        if (z+k) > 90:
            e.append(chr(64 + (z+k-90)))
        else:
            e.append(chr(z+k))
    else:
        e.append(item)
print("".join([x for x in e]))
