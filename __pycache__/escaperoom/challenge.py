while True:
    print("Welcome to the challenge! Will you be able to decipher the code to open the door?")
    print("Hello, ...!")
    key1 = input("Insert the first key to start: ")
    if key1.lower() == "world":
        break
    else:
        print("Try again...\n\n\n")

print("The first challenge was completed")

while True:
    print("Welcome to the second challenge")
    print("Maybe take a look at the door?")
    key2 = input("Insert the second key: ")
    if key2 == "KATCHOW":
        break
    else:
        print("Try again...\n\n\n")
        
print("The second challenge was completed")

while True:
    print("Welcome the the third and final challenge")
    print("Sometimes we like to store keys in files, but where?")
    print("Perhaps B107M02 knows where")
    key3 = input("Insert the third key: ")
    if key3 == "BRAWLSTARS":
        break
    else:
        print("Try again...\n\n\n")

while True:
    print("You are on the right track...")
    print("Keys are meant to be secret, try encrypting it. but how?\nACM might know...")
    key4 = input("Insert the third key: ")
    if key4 == "d1778e7b6de6c36cf6634fcb9560ab6f43c6dd38fe822575c42a6b3ee690cdf4":
        break
    else:
        print("Try again...\n\n\n")

print("You escaped, congratulations!")

