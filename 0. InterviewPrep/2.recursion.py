#1 print 1 to 100 without loop
def recursion_n(n):
    print(n)
    if n != 100:
         recursion_n(n+1) 
recursion_n(1)

#2 print factorial of number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


#3 remove all duplicates >1 count

lister = [5,2,6,4,8,7,9,8,6,5,9,9,7] 

new_list = []

for i in lister:
    if lister.count(i) == 1:
        new_list.append(i)
print(new_list)        

