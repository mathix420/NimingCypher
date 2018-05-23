from NimingCypher import NCrypter

if __name__ == "__main__":
    print('''
       _  __ _         _
      / |/ /(_)__ _   (_)___  ___ _
     /    // //  ' \ / // _ \/ _ `/
    /_/|_//_//_/_/_//_//_//_/\_, /
                            /___/
    Choose an encryption key :
        ''')
    Nkey=str(input("~: "))
    encrypter = NCrypter(Nkey)
    if encrypter.result != False:
        exit = False
    else:
        print("Fatal error !")
        exit = True

    while exit == False:
        print('''
        What do you want ?
        1 - Encrypt text
        2 - Decrypt text
        3 - Encrypt file
        4 - Decrypt file
        5 - Change key
        
        6 - Quit
        ''')
        choice = int(input("~:"))
        if choice == 1:
            print("Clear text :")
            clear_tx=str(input("~:"))
            cypher_tx = encrypter.crypt_text(clear_tx)
            print(cypher_tx)
        elif choice == 2:
            print("Cypher :")
            cypher_tx=str(input("~:"))
            clear_tx = encrypter.decrypt_text(cypher_tx)
            print(clear_tx)
        elif choice == 3:
            print("Clear file path :")
            clearpath = str(input("~:"))
            print("Encrypted file path :")
            outpath = str(input("~:"))
            sum, encrfile = encrypter.crypt_file(clearpath)
            file = open(outpath,"wb+")
            file.write(encrfile)
            file.close()
            print("Sum SHA-256 : %s" % (sum))
        elif choice == 4:
            print("Encrypted file path :")
            encrpath = str(input("~:"))
            print("Clear file path :")
            clearpath = str(input("~:"))
            file = open(encrpath,"rb")
            encrfile = file.read()
            file.close()
            sum = encrypter.decrypt_file(encrfile, clearpath)
            del encrfile
            print("Sum SHA-256 : %s" % (sum))
        elif choice == 5:
            print("Enter a new key :")
            newkey = str(input("~:"))
            encrypter.setkey(newkey)
        elif choice == 6:
            exit = True


