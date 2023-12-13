s = input("Введите строку: ")
l = len(s)
s3 = ""
s1 = ""
s2 = ""
if l%2 == 0:
    s1 = s[0:int(l/2)]
    s2 = s[int(l/2):l]
    s3 = s2 + s1
else:
    s1 = s[0:int(l/2)+1]
    s2 = s[int(l/2)+1:l]
    s3 = s2 + s1
print(s3)