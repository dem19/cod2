



for i in range(1,101):
    primo = i/i
    if primo == i:
        print(primo)

x = 100
div=0
for i in range(1,x+1):
    if x%i==0:
        div=div+1
if div>2:
     print(x,"não é primo!")
else:
    print(x,"é primo!")


