#For loop iterates a certain number of times

#Use 3 arguments in for
print('My name is')
for i in range(0, 10, 2):
    print('Jimmy' + str(i))

#Uses ranges in for
print('Yep')
for i in range(12, 16):
    print('Yep' + str(i))

#For loop is more consise then a while loop however you can do it with a while loop
#Loops for some reason
#print('My name is')
#i = 0
#while i < 5:
#    i = i + i
#    print('Jimmy Five Times' + str(i))
    

print('My name is')
#i is initilizaed with 0, so you don't have to define prior to using.
for i in range(5):
    print('Jimmy Five Times ' + str(i))

#Add 0 to 100 0+1+2+3 etc. . How to do this
total = 0
for num in range(101):
    total = total + num
print(total)