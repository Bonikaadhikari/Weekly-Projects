#Write python program to print the following patterns.
#a) *			
#  * *		       
# * * *		       
# * * * *		   
# * * * * *		   
n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end= " ")
    print()

# b) * * * * *
   # * * * *
   # * * *
   # * *
   # *
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end= " ")
    print()