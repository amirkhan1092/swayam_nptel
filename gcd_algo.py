


# program to find the gcd (greatest common divisor)

a = int(input('enter the fist number '))
b = int(input('enter the second number '))

f = 1
mi = min((a,b))

for i in range(1,mi+1):
    if a%i == 0 and b%i == 0:
        f = i

print(f)