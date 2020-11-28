a=int(input())
b=int(input())
 
def nod(n,m):
   while n!=m:
       if n>m:
           c=n-m
       else:
           c=m-n
       n=m
       m=c
   return c
print(nod(a,b))
      
