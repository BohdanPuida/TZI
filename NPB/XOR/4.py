import random
import string

print('XOR')

alphabet = list('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.,; :"1234567890-')
text = input()
key = "".join(random.choice(string.digits) for x in range(len(text)))
key1 = list()
for i in key:
    key1.append(int(i))
print(key1)
akey = {}
for i in range(0, len(alphabet)):
        akey[i+1] = alphabet[i]

cipher = list()
text = list(text)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
text_list = list()
for i in (text):
    text_list.append(get_key(akey,i))



cipher = list()
for i in range (0,len(key)):
    cipher.append(int((text_list[i]+key1[i])%len(alphabet)))


cipher_text =""
for i in cipher:
    cipher_text+=str(i)
print(cipher_text)

cipher1 = list()
for i in range (0,len(key)):
    cipher1.append(int((cipher[i]+len(alphabet)-key1[i])%len(alphabet)))



text1 = ""
for i in cipher1:
    text1+=akey.get(i)
print(text1)
input()
