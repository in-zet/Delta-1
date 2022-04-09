
e={}
a=[]
num=2
i=2
while num<=10000:
    number =num
    while i <= num :
        if num % i ==0:
            a.append(i)
            num = num / i
        else :
            i+= 1
    e[str(number)]=list(a)
    num = number +1
    a=[]
    i=2

print(e)