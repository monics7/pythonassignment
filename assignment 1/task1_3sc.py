'''3.
Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name.'''

fname=input("Enter first name:")
lname=input("Enter last name:")
rfname=fname[::-1]
rlname=lname[::-1]
print(rfname,"",rlname)
