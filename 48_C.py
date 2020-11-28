def p (g):
   n=0
   while g>0:
       j=g%10
       g=g//10
       n=n*10
       n=n+j
   return n
f=int (input())
print(p(f))
