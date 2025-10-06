import math
a = int(input())
b = int(input())
c = int(input())
if max(a, b, c) < (a + b + c) - max(a, b, c):
    cos_a = ((b**2 + c**2 - a**2)/(2*b*c))
    cos_b = ((c**2 + a**2 - b**2)/(2*a*c))
    cos_c = ((a**2 + b**2 - c**2)/(2*a*b))
print(math.degrees(math.acos(cos_a)))
print(math.degrees(math.acos(cos_b)))
print(math.degrees(math.acos(cos_c)))

