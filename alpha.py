def alpha(n):
    b=65
    k=n
    for i in range(0,n):
        for j in range(0,k):
            print(' ',end="")
        k=k-1
        for j in range(0,i+1):
            m=chr(b)
            print(m,end=" ")
            b=b+1
        print("\r")
    )
print("enter a value:")
row=int(input())
alpha(row)
                
            
