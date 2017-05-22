import random
import string
#data

alphabet = list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.,; :"1234567890-!?/+')
key = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(3))
key = set(key)
alphabet = set(alphabet)
newAlphabet = alphabet - key
#newAlphabet = sorted(newAlphabet)
newAlphabet = list(newAlphabet)
key = list(key)
dkey = {} #ключ
for i in range(0, len(key)):
    if i == 0:
        dkey[key[i]] = i
    else:
        dkey[key[i]] = 10 - i
akey = {}
for i in range(10, len(newAlphabet) + 10, 1):
    akey[newAlphabet[i - 10]] = i
#encoding
print("Write your missive\n")
text = input()
print("\n")
cipher = list()
for char in text:
    if akey.get(char):
        cipher.append(akey.get(char))
    else:
        cipher.append(dkey.get(char))
cipherf = ""
for i in cipher:
    i = str(i)
    cipherf += i
print("cypher\n")
print(cipherf)
print('\n')    #шифр


#decoding

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
entext = " "
dlist = list()
n = len(dkey)
dlist.append(0)
for i in range(2,n+1):
    dlist.append(9 - n + i)
b = list(cipherf)
res = []
ban = []
for x in range(len(cipherf)):
    if x in ban:
        continue

    t = b[x]
    if float(t) in range(1, 8):
        if x + 1 < len(cipherf):
            ban.append(x+1)
            tl = t + b[x+1]
        else:
            tl = t
    else:
        tl = t
    res.append(int(tl))
for i in range(0, len(res), 1):
   if res[i] == dlist[1] or res[i]==dlist[0] or res[i]==dlist[2]:

     t = ""
     t = get_key(dkey, res[i])
     t = str(t)
     entext += t

   else:
     a = res[i]
     h = ""
     h = get_key(akey, a)
     h = str(h)
     entext += h

#results
print("key\n")

print(dkey)

print("\n")

print("encoded text\n")
print(entext)
print("\n")
print("Press enter to exit")
print("\n")
input()
