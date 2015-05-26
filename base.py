# -*- coding: utf-8 -*-


num = 8080
print(num)

numStr = str(num)
print(numStr)

# numStr = "100t"
num = int(numStr)
print(num)

f = float(numStr)
print(f)



cron = [('0 0 10,14,16 * * ?',2)]

for one in cron:
    print(one[0], "-----", one[1])
    h = one[0].split(" ")
    print(len(h))
    for oneStr in h:
        print(oneStr)



print('------------------------------')


a = {'person':{'name':'tao','age':18}}
for one in a:
    print(one)
    print(a.get(one))
