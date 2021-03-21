n=int(input("Enter the no. of terms for FIBONACCI : "))
first=0
second=1
sum=0
count=0
while count<n:
    print(first,end=",")
    sum=first+second
    first=second
    second=sum
    count+=1
