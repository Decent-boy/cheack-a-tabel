# tabel
user=int(input("enter a value where you want to take a tabel: "))
def mul(n):
    for i in range(user+1):
        print(f"\n{n}*{i}={n*i}")
n=int(input("enter value of tabel: "))
mul(n)