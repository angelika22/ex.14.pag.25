x=int(input("dati numarul liniei a matricei="))
B=[[int(input()) for i in range(x)] for n in range(x)]
print("matricea-")
for i in range(len(B)):
    print(B[i])
sum1=0
for i in range(0, len(B)):
    sum1+=B[i][i]
sum2=0
for i in range(0, len(B)):
    sum2+=B[len(B)-i-1][i]
print("suma componentelor diagonalei secundare=", sum2)
print("suma componentelor diagonalei principale=", sum1)
sum3=0
for i in B:
    for n in i:
        if B.index(i)<i.index(n):
            sum3+=n
print(f"suma componentelor mai sus de diagonala principala-", sum3)
sum4=0
for i in B:
    for n in i:
        if B.index(i)>i.index(n):
            sum4+=n
print(f"suma componentelor mai jos de diagonala principala-", sum4)
sum5=0
for i in B:
    for n in i:
        if B.index(i)+i.index(n)<n-1:
            sum5+=n
print(f"suma componentelor mai sus de diagonala secundara-", sum5)
sum6=0
for i in B:
    for n in i:
        if B.index(i)+i.index(n)>n-1:
            sum6+=n
print(f"suma componentelor mai jos de diagonala secundara-", sum6)





