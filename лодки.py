m = int(input('Максимальная масса, которую выдержит лодка '))
n = int(input('Количество рыбаков '))
k =[]
l=0
for i in range(n):
    a=int(input('Масса рыбака '))
    k.append(a)
l=0
for i in range(n):
    if(k[i]+k[i])<=m:
        l=l+1
print(l)    
        

       

