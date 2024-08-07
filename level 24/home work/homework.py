#      -10  -9 -8 -7 -6 -5 -4 -3 -2  -1
listn = [1 ,2 ,3 ,4 ,5 ,6 , 7, 8, 9, 10]
#        0 1 2 3 4 5 6 7 8 9

print(listn[0:3])
print(listn[7:10])
print(listn[3:7])

print(listn[-10:-7])
print(listn[-3:])
print(listn[-7:-3])

name = "hello i am 10 years old"


print(name[0:5])
print(name[6])
print(name[8:10])
print(name[11:13])
print(name[14:19])
print(name[20:23])

hello = "Hello, World!"

for i in hello:
    print(i)


counter = 0

while counter < 10:
    counter += 1
    print(counter)

sum = 0
i = 0


while i < 100:
    i += 1
    if i < 50 or i > 60:
        sum += i
print(sum)


sum = 0
i = 0

while sum < 50:
    i += 1
    sum += i
print(sum)