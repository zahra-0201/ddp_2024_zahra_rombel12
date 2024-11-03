a = 1
while a<=5 :
    print(a)
    a += 1

b = 1
while b<=10 :
    print(b, "zahra") #untuk nama berulang
    b += 1

#bilangan ganjil
c = 1
d = "jeje"
while c<=10 :
    print(c, d)
    c += 1
n = 1
while n<=19 :
    print(n)
    n +=2

#while bertingkat
j = 1
while j<=10 :
    k = 1
    while k<=10 :
        print(j*k, end="")
        k+=1
    print()
    j+=1

#awal, akhir, step = 1, 10, 3 = 1+3= 4, 4+3=7
#bilangan ganjil kurang dari 20
for a in range (1, 20, 2) :
    print(a)

#nama sampai 20 kali
for i in range(1, 21) :
    print(i, "zahra")

#for bertingkat
for i in range (1, 11):
    for j in range (1, 11):
        k = i*j
        print(k, end=" ")
print("")

i = 1
while i<6 :
    print(i)
    if i == 3:
        break
    i +=1
