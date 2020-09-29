from Crypto.Cipher import AES
import random

def test():
    Challenge = bytearray(8)
    Credentials = bytearray(8)
    print("test1: all zeros challenge\n");
    simulate_netlogon_auth(Challenge,Credentials)
    print("test2: identicle bytes challenge\n");
    Challenge = bytearray([7,7,7,7,7,7,7,7])
    simulate_netlogon_auth(Challenge,Credentials)
    print("test3: Changing last byte challenge\n");
    Challenge = bytearray([7,7,7,7,7,7,7,8])
    Credentials[7] = 15 # 7 XOR 8
    simulate_netlogon_auth(Challenge,Credentials)
    print("test4: Changing the byte before last byte challenge\n");
    Challenge = bytearray([7,7,7,7,7,7,8,6]) #6 is arbitrary
    Credentials[6] = 15 # 7 XOR 8
    Credentials[7] = 9 #arbitrary
    simulate_netlogon_auth(Challenge,Credentials)
    

    
    

def simulate_netlogon_auth(Challenge,Credentials):

    iv = bytearray(16)

    key = bytearray(16)
   
    enc  = bytearray(8)
    enc[0] = 1
    j = 0
    while (enc != Credentials):
        key = bytearray((random.getrandbits(8) for i in range(16)))
        cipher = AES.new(key, AES.MODE_CFB, iv)
        enc = cipher.encrypt(Challenge)
        j = j + 1
      
    print("guess #" + str(j) + " Challenge: " + Challenge.hex() + " key: " + key.hex() + " Credentials: " + enc.hex() + "\n")
