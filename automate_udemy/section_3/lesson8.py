#Built in functions
#print(), input(), len()
import random, sys, os, math

#To recap lesson 8, You can import modules and get acces to new function
#The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool
#Use sys.exit function to quit immedietly
#pyperclip has copy and post functions for reading and writing text to the clipboard

#how to install pyperclip
import pyperclip
pyperclip.copy('Hello World')
pyperclip.paste()


#pip is a tool used to import https://automatetheboringstuff.com/appendixa/

#if you do from random import *
#You don't need to preceed with random so randint(1, 10)

#How do you terminate a program early
#call sys.exit()

#Uses random integer function from random library
print(random.randint(1, 10))
sys.exit()
print('Something Else')
