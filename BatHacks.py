import base64
def intro():  
  print(r"""
    ._.                 _.____.
     ) \              /    .(
     )  |            .'   .(
     ). ).          .'  .(
       ) |.        .'  (
       ). ;      ./  .(
        ) |      )  (
        ).;      :.(
         )|    .|.;
         .^--^./ (.
         ;0..0;   b
          'vv'_.:_.;  made by: SeaBass4201759
               m  M
  ▀█████████▄     ▄████████     ███             ▄█    █▄       ▄████████  ▄████████    ▄█   ▄█▄    ▄████████ 
    ███    ███   ███    ███ ▀█████████▄        ███    ███     ███    ███ ███    ███   ███ ▄███▀   ███    ███ 
    ███    ███   ███    ███    ▀███▀▀██        ███    ███     ███    ███ ███    █▀    ███▐██▀     ███    █▀  
  ▄███▄▄▄██▀    ███    ███     ███   ▀       ▄███▄▄▄▄███▄▄   ███    ███ ███         ▄█████▀      ███         
  ▀▀███▀▀▀██▄  ▀███████████     ███          ▀▀███▀▀▀▀███▀  ▀███████████ ███        ▀▀█████▄    ▀███████████ 
    ███    ██▄   ███    ███     ███            ███    ███     ███    ███ ███    █▄    ███▐██▄            ███ 
    ███    ███   ███    ███     ███            ███    ███     ███    ███ ███    ███   ███ ▀███▄    ▄█    ███ 
  ▄█████████▀    ███    █▀     ▄████▀          ███    █▀      ███    █▀  ████████▀    ███   ▀█▀  ▄████████▀  
                                                                                      ▀                      """) 
#base64 encryption function
def base64_encryption():
  encypt_This_Bitch = input('\nEnter what you want to encrypt in Base64: ')
  encode64 = base64.b64encode(encypt_This_Bitch.encode("utf-8"))
  messge = print(f"\nEncrypted message: {encode64}") 
#base64 decrytpin function 
def base64_decryption():
  decrypt_This_Bitch = input('\nEnter what you want to decrypt in Base64: ')
  decode64 = base64.b64decode(decrypt_This_Bitch.encode("ascii"))
  print(f"\nDecrypted message: {decode64}")
#port scanning function
def da_portscanner():
  print("\nStill in the works.")
def bat_encrypt():
  secret_bat_message = input("Enter what you want to encrypt: ")
  daList = []
  for char in secret_bat_message:
    dVal = [ord(char)]
    popval = dVal.pop(0)
    popval = int(popval)
    daList.append(bin(popval))
  print(":".join(daList)) #The binary val is 'str'
########### The brains of the operation ################
intro()
def daBrain():
  #bat hacks options
  selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.port scanning\n3.Exit\nEnter choice: ')
  #loop
  while selection == '1' or '2' or '3': 
    #Cryptography
    if selection == '1':
      cryp_choice = input("\nWelcome to the cryptography section. What do you want to use?\n1.Base64\n2.Bat-ography\nEnter choice: ")
      if cryp_choice == '1':
        en_decryp = input("\nWhat would you like to do?\n1. Encryption \n2. Decryption\nEnter choice: ")
        if en_decryp == '1':
          base64_encryption()
          selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.port scanning\n3.Exit\nEnter choice: ')
        elif en_decryp == '2':
          base64_decryption()
          selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.port scanning\n3.Exit\nEnter choice: ')
      #bat-ography
      elif cryp_choice == '2':
        bat_encrypt()
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.port scanning\n3.Exit\nEnter choice: ')  
      else:
        cryp_choice = input("\nWelcome to the cryptography section. What do you want to use?\n1.Base64\n2.Bat-ography\nEnter choice: ")
    #Port scanning 
    elif selection == '2':
      da_portscanner()
      selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.port scanning\n3.Exit\nEnter choice: ')
    #exit
    elif selection == '3':
      exit()
    #loop back
    else:
      selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.port scanning\n3.Exit\nEnter choice: ')
daBrain()
