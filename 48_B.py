def summa (k):
    sum =0
    while k!=0:
        sum+=k%10
        k=k//10
    return sum
f= int (input())
print(summa(f))
