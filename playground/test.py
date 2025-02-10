from decimal import Decimal
# x = 0.1 + 0.2
# y = 0.3
# if abs(x - y) < 1e-10:
#     print("x and y are equal")
# else:
#     print("x and y are not equal")
# # print(x == y) 

N = 1000000
res = Decimal(100.0)
h = res / Decimal(N)
x = Decimal(0.0)
for i in range(N):
    x += h

print(x == res)
print(f"{x - res}")