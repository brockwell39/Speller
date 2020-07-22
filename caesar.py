from sys import argv
from cs50 import get_string
# checks user has provided a comand line argument
if len(argv) == 2:
    k = argv[1]
    k = int(k)
# if k is abouve 26 modulates
    if k > 26:
        k = k % 26
# asks user for plaintext
    p = get_string("Plaintext: ")
    print("ciphertext: ", end="")
# goes through string and sees if alpha if alpha changes by k if not prints
    for c in p:
        if c.isalpha() == True:
            if c.isupper() == True:
                n = ord(c)
                n = n + k
                # if beyond capital asciii range modulates to bring back
                if n > 90:
                    n = (n % 90) + 64
                    print(chr(n), end="")
                else:
                    print(chr(n), end="")
            # handles lowercase letters
            else:
                n = ord(c)
                n = n + k
                # if beyond lowercase asciii range modulates to bring back
                if n > 122:
                    n = (n % 122) + 96
                    print(chr(n), end="")
                else:
                    print(chr(n), end="")
        else:
            print(c, end="")
    print()
else:
    print("Usage:caesar.py key")
    exit(1)
