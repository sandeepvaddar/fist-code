def is_leap(n):
    if n%400==0:
        return True
    if n%100==0:
        return False
    if n%2==0:
        return False
    year = int(input())
    print(is_leap)