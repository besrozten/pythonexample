def encrypt(plain, key):
    # type: (str, int) -> str

    # TODO your code will be here
    # this is new comment

    sifreliYazı=[]

    for x in plain:

        if x.isupper():
            # alphabet[(alphabet.index(x) + 3) % len(alphabet)]

            formul = ((ord(x) - 65) + key) % 26
            sifreliYazı.append(chr(formul + 65))
        elif x.islower():
            formul = ((ord(x) - 97) + key) % 26
            sifreliYazı.append(chr(formul + 97))
        else:
            sifreliYazı.append(x)
    return "".join(sifreliYazı)



def decrypt(encrypted, key):
    # type: (str, int) -> str

    # TODO your code will be here
    sifreliYazı=[]

    for x in encrypted:
        if x.isupper():
            formul = ((ord(x) - 65) - key) % 26
            if formul <0:
                formul+=26
            sifreliYazı.append(chr(formul + 65))
        elif x.islower():
            formul = ((ord(x) - 97) - key) % 26
            if formul <0:
                formul+=26
            sifreliYazı.append(chr(formul + 97))
        else:
            sifreliYazı.append(x)
    return "".join(sifreliYazı)




if __name__ == '__main__':
    plain = "Hello, World!"
    key = 10

    encrypted = encrypt(plain, key)
    decrypted = decrypt(encrypted, key)

   # if encrypted or decrypted is None:
     #   exit(1)

    print("plain: %s " % plain)
    print("key:  %d " % key)
    print("encrypted:  %s " % encrypted)
    print("decrypted :  %s " % decrypted)
