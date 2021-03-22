a=input("enter the Values : ")  #1,4,2,5,3
b=a.split(",")
c=[]
for i in range(len(b)):
    c.append(int(b[i]))
t=len(c)
sm=0
total=0;
while sm<t-2:
    n=c[sm]+c[sm+1]+c[sm+2]
    total = total + n;
    sm=sm+1
k=sum(c)
final_sum=total+2*k
print(final_sum)
