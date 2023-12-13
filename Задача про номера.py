import re

phone = input("Введите номер ")
print("phone =", phone, type(phone))

if re.fullmatch(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', phone):
    print("Номер корректен")
else:
    print("Неккоректный номер телефона")
    exit(1)

phoneBook = [phone, '8(495)430-23-97', '+7-4-9-5-43-023-97', '4-3-0-2-3-9-7',
             '8(904)-346-04-88']
phoneBook += ['8-495-430']

print("phoneBook = ", phoneBook)
phoneBookNew = [s.replace('-','').replace(' ','').replace('(', '').replace(')', '') for s in phoneBook]

for i in range(len(phoneBookNew)):
    if len(phoneBookNew[i]) == 7:
        phoneBookNew[i] = '+7495' + phoneBookNew[i]
    elif len(phoneBookNew[i]) == 10:
        phoneBookNew[i] = '+7' + phoneBookNew[i]
    elif(phoneBookNew[i][0] == '8'):
       # phoneBookNew[i] = '+7' + phoneBookNew[i][1:]
        phoneBookNew[i] = phoneBookNew[i].replace('8', '+7', 1)

for i in range(1, len(phoneBookNew)):
    if (phoneBookNew[0] == phoneBookNew[i]):
        print("YES")
    else:
        print("NO")
