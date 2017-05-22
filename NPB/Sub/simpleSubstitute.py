import random


def encrypt(text,z):
    textSize = len(text)
    difference = (textSize) % z
    if difference != 0:

        for i in range(0,z - difference):
            text += chr(random.randrange(ord('a'), ord('z'), 1))

        textSize = len(text)

    newcode = ""
    for k in range(0,z):
     for i in range(k,textSize,z):
        newcode += text[i]
    return newcode


def decrypt(text,z):
    textSize = len(text)
    a = textSize/z
    a = int(a)
    newcode = ""
    for k in range(0,a):
     for i in range(k,textSize,a):
        newcode += text[i]
    return newcode
print('SimpleSub')
mes = input()
print(encrypt(mes,2))
print(decrypt(encrypt(mes,2),2))

input()