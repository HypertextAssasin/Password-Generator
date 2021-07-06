import random

def StringShuffler(string):
    slist=list(string)
    random.shuffle(slist)
    return ''.join(slist)


UppercaseLetter1=chr(random.randint(65,90))
UppercaseLetter2=chr(random.randint(65,90))
LowercaseLetter1=chr(random.randint(97,122))
LowercaseLetter2=chr(random.randint(97,122))
Digit1=chr(random.randint(48,57))
Digit2=chr(random.randint(48,57))

password= UppercaseLetter1 + UppercaseLetter2 + LowercaseLetter1 + LowercaseLetter2 + Digit1 + Digit2
StringShuffler(password)

print("your password is",password)