n=int(input())
a=1
if n==1 or n==2:
    print("Yes")
else:
    for i in range(n-1):
        a=a+1
        if n%a==0:
            print("No")
            break
        
        

