def max(a, s):
    if a > s:
        return a
    else:
        return s
def min(a, s):
    if a < s:
        return a
    else:
        return s
print("vvedite 4 chisla")
z = int(input())
x = int(input())
c = int(input())
v = int(input())
max1 = max(max(z,x),max(c,v))
max2 = min(min(z,x),min(c,v))
print("max = ",max1)
print("min = ",max2)
summ = max1+max2
print("summa = ",summ)