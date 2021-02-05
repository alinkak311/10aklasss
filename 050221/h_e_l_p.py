#9.42

s1 = input('vvedi slovo')

s2 = s1[::-1]

print (s2)
__________________________

#9.44

s = input ('vvedi slovo')

t = s[::-1]

print (t)
_____________________________

#9.45

s = "*"

print (s*5)
________________________________

#9.46

y = "-"

print (y*8)
________________________________

#9.47

ch = int(input ('vvedite chislo'))

sim = input('vvedite simvol')

print (sim * ch)
_________________________________

#9.48

sl = input('vve slovovo')

print (4*"+", sl, 5*"-")
____________________________________

#9.49

slovo = input ('vvedite slovo')

a = len (slovo)

print ("*" * a)
________________________________________

#9.59

s = input ('vvedi slovo')

gl = "о"
k= 0
for i in s:
    if i in gl:
        k+=1
print ('kolichestvo ', k)
______________________________________

#9.66

d =  input ('vvedi predlozheie')

a = d.split()

print('naydeno slov ', len(a))
___________________________

#9.67

pred =  input ('vvedi predlozhenie')

a = pred.split()

print('naydeno slov ', len(a))
_____________________________________

#9.68

s = input ('vvedi text')

plys = "+"
k= 0
for i in s:
    if i in plys:
        k+=1
podch = "-"        
z = 0

for j in s:
    if j in podch:
        z+=1
print ('kolichestvo "-" ', z)        
print ('kolichestvo "+" ', k)
_____________________________________

#9.70

s = input ('vvedi text')

glasny = "аеёиуоыэюя"
k= 0
for i in s:
    if i in glasny:
        k+=1
print ('kolichestvo ', k)
_______________________________________

#9.71

s = input ('vvedi slovo')

k = "н"
n= 0
for i in s:
    if i in k:
        n+=1

v = "м"
m = 0
for j in s:
    if j in v:
        m +=1
        
print ('kolichestvo "н" ', n)
print ('kolichestvo "м" ', m)


if n == m:
    print ("н", "=", "м")
elif n > m:
    print ("н" , ">", "м")
else:
    print ("н", "<", "м")
_____________________________________________

#9.172

n = input('vvedite text')

a = n.split()

l = 0

for i in range(len(a)):

   if len(a[i]) > l:

       l = len(a[i])

       ll = a[i]

print(ll, "длина ", l)
