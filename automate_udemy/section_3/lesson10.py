
#local eggs 99 variable is printed not the eggs = 0 in bacon

ham = 68

def spam():
    eggs = 99
    bacon()
    print(eggs)
    #print(ham) # causes error ham undefined
    ham = 42
    print(ham)

def bacon():
    print(ham)
    eggs = 0


spam()
bacon()