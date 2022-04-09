#Soloution of Problem number 1
t,n = input().split()
t,n = int(t),int(n)

#Mathematical Formula: t = d + Σ(d/2^i) | 1 <= i < n 
x = 1
for i in range(1,n):
    x += (1/2**i)
print("{:.4f}".format(t/x))