'''2.
Create the below pattern using nested for loop in Python.'''
n=5;
# TOP Pattern
for i in range(0,n):
    for j in range(0,i):
        print ('* ', end="")
    print('')

# Bottom pattern
for i in range(n,0,-1):
    for j in range(0,i):
        print('* ', end="")
    print('')
