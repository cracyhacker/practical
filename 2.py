a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))
largest = 0
smallest = 0
#greatest
if a > b and a > c:
    largest = a
if b > a and b > c:
    largest = b
if c > a and c > b:
    largest = c
#smallest
if a < b and a < c:
    smallest = a
if b < a and b < c:
    smallest = b
if c < a and c < b:
    smallest = c
print(largest, "is the largest of three numbers.")
print(smallest, "is the smallest of three numbers.")