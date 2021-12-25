#series 1
# x = float(input("Enter value of x :"))
# n = int(input("Enter value of n :"))
# s = 0
# for a in range(n+1):
#     s += x**a
# print("Sum of series", s)

#Series 2
# x = float(input("Enter value of x :"))
# n = int(input("Enter value of n :"))
# s = 0
# for a in range (n+1):
#     if a%2==0:
#         s += x**a
#     else:
#         s -= x**a
# print("sum of series", s)        

# Series 3 
x = float(input("Enter value of x :"))
n = int(input("Enter value of n :"))
s = 0
z = 1.0
for a in range (n):
    a += 1
    z = z*a
    if a%2==0:
        s += (x**a)/z
    else:
        s -= (x**a)/z
print("sum of series", s) 