n1,n2,n3,n4 = map(int,input().split())
m1,m2,m3,m4 = map(int,input().split())

Gunnar = n1+n3+n2+n4
Emma = m1+m2+m3+m4

if Gunnar > Emma:
    print("Gunnar")
elif Emma > Gunnar:
    print("Emma")
else:
    print("Tie")