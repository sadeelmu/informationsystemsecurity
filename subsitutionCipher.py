# Symmetric Encryption
import string

# The Symmetric Cipher model is composed of five parts:
# 1. Plain Text, var x:
    # This is the original data/message that is to be communicated to the receiver by the sender.
    # It is one of the inputs to the encryption algorithm.

# 2. Secret Key, var k:
    # It is a value/string/textfile used by the encryption and decryption algorithm to encode and decode the plain text to cipher text and vice-versa respectively.
    # It is independent of the encryption algorithm.
    # It governs all the conversions in plain text. All the substitutions and transformations done depend on the secret key.

# 3. Encryption Algorithm, var E:
    #  It takes the plain text and the secret key as inputs and produces Cipher Text as output.
    # It implies several techniques such as substitutions and transformations on the plain text using the secret key.

# 4. Cipher Text, var y:
    # It is the formatted form of the plain text (x) which is unreadable for humans, hence providing encryption during the transmission.
    # It is completely dependent upon the secret key provided to the encryption algorithm. Each unique secret key produces a unique cipher text.

# E(x, k) = y

# 5. Decryption Algorithm, var D:
    # It performs reversal of the encryption algorithm at the recipient’s side.
    # It also takes the secret key as input and decodes the cipher text received from the sender based on the secret key.
    # It produces plain text as output.

#D(y, k) = x

# Substitution Cipher

#(Encryption Phase with shift n)
# En(x) = (x + n) mod 26

#(Decryption Phase with shift n)
# Dn(x) = (x - n) mod 26

plainText = "StrInGoFbothLowerandUPPERChars"
cipherText = []
charsOfTheAlphabet = string.ascii_letters
key = 4
dict_sub = {}

#checks
if(plainText.isupper() or plainText.islower() or (not plainText.isalpha())):
        print("Not valid input")

for i in range(len(charsOfTheAlphabet)):
    dict_sub[charsOfTheAlphabet[i]] = charsOfTheAlphabet[i+key%len(charsOfTheAlphabet)]

for char in plainText:
    if char in charsOfTheAlphabet:
        temp = char
        cipherText.append(temp)
    else:
        temp=char
        cipherText.append(temp)

cipherText = "".join(cipherText)
print("cipher is " ,cipherText)