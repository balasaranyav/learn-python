n=int(input("Enter Number :"))
t={}
sum=0
for i in range(n):
    t[i]=input("Input :")
k=int(input("Enter Value :"))
for j in range(0,k):
    m = t[j]
    sum += m
print(sum)