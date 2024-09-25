import base64
def intro():  
  print("""
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
  encypt_This_Bitch = input('Enter what you want to encrypt in Base64: ')
  encode64 = base64.b64encode(encypt_This_Bitch.encode("utf-8"))
  print(encode64)
#base64 decrytpin function 
def base64_decryption():
  decrypt_This_Bitch = input('Enter what you want to decrypt in Base64: ')
  decode64 = base64.b64decode(decrypt_This_Bitch.encode("ascii"))
  print(decode64)


########### The brains of the operation ################
intro()
def daBrain():
  #bat hacks options
  selection = input('Welcome to BatHacks choose what you want to do: \n1.Encrpyt and decrypt in base64 \n2.port scanning\n3.Exit\nEnter choice: ')
  
  while selection == '1' or '2' or '3': 
    if selection == '1':
      base_choice = input("Please select what you want to do with base64: \n1.Encryption\n2.Decryption\nEnter choice: ")
      if base_choice == '1':
        base64_encryption()
        selection = input('Welcome to BatHacks choose what you want to do: \n1.Encrpyt and decrypt in base64 \n2.port scanning\n3.Exit\nEnter choice: ')
      
      elif base_choice == '2':
        base64_decryption()
        selection = input('Welcome to BatHacks choose what you want to do: \n1.Encrpyt and decrypt in base64 \n2.port scanning\n3.Exit\nEnter choice: ')
        
    elif selection == '2':
      print("Let's scan some ports!")
      ip = input("what is the ip you want to scan?")
      print("TO BE CONTINUED uWu")
      selection = input('Welcome to BatHacks choose what you want to do: \n1.Encrpyt and decrypt in base64 \n2.port scanning\n3.Exit\nEnter choice: ')
      
    elif selection == '3':
      exit()
    
    else:
      selection = input('Welcome to BatHacks choose what you want to do: \n1.Encrpyt and decrypt in base64 \n2.port scanning\n3.Exit\nEnter choice: ')
      
daBrain()