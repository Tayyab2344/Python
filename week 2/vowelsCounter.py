a = input("Enter a String: ")
length = len(a)
count = 0
for i in range(length):
    if a[i] in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:  
        count += 1 
        print(a[i]) 
print(count)
