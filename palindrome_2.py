n = int(input("Enter a number: "))
z = 0
t= n
while n > 0:
   r = n % 10
   z=z*10+r
   n //= 10
if t==z:
   print(n,"It's a Palinrome")
else:
   print(n,"is not an Palindrome")