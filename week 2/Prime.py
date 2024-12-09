a = int(input("Enter a number  : "))
isPirme = 1
for i in range(2,a-1):
    if(a%i == 0):
        isPirme = 0
if(isPirme):
        print("Prime")
else:
        print("Not a prime")    
