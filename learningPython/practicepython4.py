"""
LOOPS
WHILE LOOP
"""

counter = int(input("Enter Number:"))

while counter > 0:
    counter = counter - 1
    print (counter)
if counter < 0:
    print ("Game over")

#using while loop to create a program that accepts input from users and multiplies it.

num = int(input("Enter a number:"))
COUNTER = 0
while counter <= 20:
    result = ( num * counter)
    print(num, "*", counter, "=", result)
    counter = counter + 1


#for loop
te_st = "life"
for character in te_st:
    print(te_st)
