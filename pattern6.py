n=int(input())
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(' ',end="")
        space=space+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1