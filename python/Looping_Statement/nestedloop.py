#nested loop
''' nested loop is a loop inside a loop. it is used to execute a block of code
repeatedly until a certain condition is met. '''

for i in range(3):
    for j in range(3):
        print(i, j)


#Q. write a nested loop to print the multiplication table of 1 to 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

#Q. write a nested loop to print the pattern of stars.
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

#Q. write a nested loop to print the pattern of numbers.
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



for i in range(1, 11):
    for j in range(1, 11):
       a= i * j 
       if a%2 == 0 :
           print("*", end=" ")
       else:
           print(" ", end=" ")
    print()
