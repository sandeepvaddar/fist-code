n = int(input("Enter n :"))
s = 0
t = n

while n !=0:
    ld = n % 10
    s = s + ld  #last digits(ld)
    n = n // 10
print("Sum of digits pf ", t, "is",s)
