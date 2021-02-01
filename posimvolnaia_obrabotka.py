s = input ("Vvedite imia ")
l = ""             #замена "а"

for c in s:
    if c == "а":
        c="б"
    l = l + c
print (l[:1])

o =""           #замена "б"
for k in s:
    if k == "б":
        k="а"
    o = o + k
print (o[2:3])


m =""           #замена "А"
for p in s:
    if p == "А":
        p ="Б"
    m = m + p
print (m[4:5])


u =""           #замена "А"
for q in s:
    if q == "Б":
        q ="А"
    u = u + q
print (u[6:7])

y =""           #замена "с"
for t in s:
    if t == "c":
        t ="c"
    y = y + t
print (y[8:9])

n =""           #замена "с"
for e in s:
    if e == "С":
        e ="С"
    n = n + e
print (n[10:11])



print (l[:1]*2+o[2:3]*2+m[4:5]*2+u[6:7]*2+y[8:9]*2+n[10:11]*2)
