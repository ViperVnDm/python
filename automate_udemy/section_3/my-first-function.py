import random
import sys
#If you want to do from random import * then prefix.function is not needed. 

print(random.randint(1, 10))

#how to terminate early? 

#New function
def hell0():
    print('Howdy')
    print('Howdy1')
    print('Howdy2')

hell0()
hell0()

username = input('Enter your login user: ')

#Define the function to reduce recurring code
def gcloudlogin(name):
    'gcloud auth login' + name

gcloudlogin(username)

#how to terminate early?
return