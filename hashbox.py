#!/usr/bin/env python3

# Date: 12/12/2022
# Author: Furkan
# Github: @Kerxunos
# Description: Hash-Encryption decoder-encoder MultiFunction Tool
import os
from time import sleep
from sys import exit
import codecs
try:
    import hashlib
    import base64
    from colorama import Style,Fore,init
except ModuleNotFoundError as e:
    qs = input("[?] Would you like to download the required modules ? (Y/n)")
    if(qs == "Y" or qs == "y"):
        os.system("pip install colorama")
        os.system("pip install hashlib")
        os.system("pip install base64")
    if(qs == "N" or qs == "n"):
        exit()
#-TR-#
#10/12/2022 @Kerxunos tarafından yapılan uygulama uygulama kullanıma hazır hale getirildi
#Debug tarihi: 11/12/2022
#Bir sonraki Debug tarihi 12/12/2022
#Eklenecekler: Rot47 ve çeşitli Rot türlerinin yanında yeni Hash-Encoding çeşitleri kullanıma hazır hale getirilecek

#-EN-#
#10/12/2022 the application maded by @Kerxunos now be avabile for using
#Last Debug date: 11/12/2022
#Next Debug date: 12/12/2022 
#Rot47 and more Rot types and Hash-Encodings will adding in next days

print("    __  __           __    ____              ")
print("   / / / /___ ______/ /_  / __ )____  _  __ ®")
print("  / /_/ / __ `/ ___/ __ \/ __  / __ \| |/_/  ")
print(" / __  / /_/ (__  ) / / / /_/ / /_/ />  <    ")
print("/_/ /_/\____/____/_/ /_/_____/\____/_/|_|    ")
print("  Made By @Kerxunos                     v1.84")
sleep(2)
enc_dcd = input("Encoding or Decoding? (E/D): ")
if(enc_dcd == "D" or enc_dcd == "d"):
    print("Supported Hash-Encoding Type: md5, sha1, sha256, sha512, sha384, sha224, base16, base32, base64, base85, rot13")
    hashtype = input("Hash-Encoding Type: ")
    if(hashtype == "md5" or hashtype == "sha1" or hashtype == "sha256" or hashtype == "sha512" or hashtype == "sha384" or hashtype == "sha224"):
        wordlist = str(input("Wordlist path: "))
        f = open(f"{wordlist}","r")
        tanım = str(input("giriş: "))
        line = f.readlines()
        count = len(line)
    password = input("Hash-Encoding: ")
    sayac = 0
    #MD5
    if(hashtype == "md5"):
        for i in line:
            up_word = line[sayac]
            zxc = up_word.strip()
            hashed = hashlib.md5(zxc.encode())
            hashed = hashed.hexdigest()
            print(Fore.WHITE + "[-] Attack Informations...")
            print(Fore.WHITE + f"[-] Wordlist: {wordlist}")
            print(Fore.WHITE + f"[-] Hash-Type: {hashtype}")
            print(Fore.WHITE + f"[-] Hash: {password}")
            print(Fore.WHITE + f"[-] Word: {zxc}")
            print(Fore.WHITE + f"[-] Trying: {hashed}")
            print(Fore.WHITE + f"[-] Progress: {sayac}/{count}")
            sayac += 1
            sleep(0.000001)
            if(hashed == password):
                break
            os.system("cls")
        if(hashed == password):
            print(Fore.GREEN + "---------! Hash Cracked !----------")
            print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
            print(Fore.GREEN + f"[+] Password: {zxc}" + Style.RESET_ALL + Fore.RESET)
            sleep(3)
    #SHA1
    if(hashtype == "sha1"):
        for i in line:
            up_word = line[sayac]
            zxc = up_word.strip()
            hashed = hashlib.sha1(zxc.encode())
            hashed = hashed.hexdigest()
            print(Fore.WHITE + "[-] Attack Informations...")
            print(Fore.WHITE + f"[-] Wordlist: {wordlist}")
            print(Fore.WHITE + f"[-] Hash-Type: {hashtype}")
            print(Fore.WHITE + f"[-] Hash: {password}")
            print(Fore.WHITE + f"[-] Word: {zxc}")
            print(Fore.WHITE + f"[-] Trying: {hashed}")
            print(Fore.WHITE + f"[-] Progress: {sayac}/{count}")
            sayac += 1
            sleep(0.000001)
            if(hashed == password):
                break
            os.system("cls")
        if(hashed == password):
            print(Fore.GREEN + "---------! Hash Cracked !----------")
            print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
            print(Fore.GREEN + f"[+] Password: {zxc}" + Style.RESET_ALL + Fore.RESET)
            sleep(3)
    #SHA256
    if(hashtype == "sha256"):
        for i in line:
            up_word = line[sayac]
            zxc = up_word.strip()
            hashed = hashlib.sha256(zxc.encode())
            hashed = hashed.hexdigest()
            print(Fore.WHITE + "[-] Attack Informations...")
            print(Fore.WHITE + f"[-] Wordlist: {wordlist}")
            print(Fore.WHITE + f"[-] Hash-Type: {hashtype}")
            print(Fore.WHITE + f"[-] Hash: {password}")
            print(Fore.WHITE + f"[-] Word: {zxc}")
            print(Fore.WHITE + f"[-] Trying: {hashed}")
            print(Fore.WHITE + f"[-] Progress: {sayac}/{count}")
            sayac += 1
            sleep(0.000001)
            if(hashed == password):
                break
            os.system("cls")
        if(hashed == password):
            print(Fore.GREEN + "---------! Hash Cracked !----------")
            print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
            print(Fore.GREEN + f"[+] Password: {zxc}" + Style.RESET_ALL + Fore.RESET)
            sleep(3)
    #SHA512
    if(hashtype == "sha512"):
        for i in line:
            up_word = line[sayac]
            zxc = up_word.strip()
            hashed = hashlib.sha512(zxc.encode())
            hashed = hashed.hexdigest()
            print(Fore.WHITE + "[-] Attack Informations...")
            print(Fore.WHITE + f"[-] Wordlist: {wordlist}")
            print(Fore.WHITE + f"[-] Hash-Type: {hashtype}")
            print(Fore.WHITE + f"[-] Hash: {password}")
            print(Fore.WHITE + f"[-] Word: {zxc}")
            print(Fore.WHITE + f"[-] Trying: {hashed}")
            print(Fore.WHITE + f"[-] Progress: {sayac}/{count}")
            sayac += 1
            sleep(0.000001)
            if(hashed == password):
                break
            os.system("cls")
        if(hashed == password):
            print(Fore.GREEN + "---------! Hash Cracked !----------")
            print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
            print(Fore.GREEN + f"[+] Password: {zxc}" + Style.RESET_ALL + Fore.RESET)
            sleep(3)
    #SHA384
    if(hashtype == "sha384"):
        for i in line:
            up_word = line[sayac]
            zxc = up_word.strip()
            hashed = hashlib.sha384(zxc.encode())
            hashed = hashed.hexdigest()
            print(Fore.WHITE + "[-] Attack Informations...")
            print(Fore.WHITE + f"[-] Wordlist: {wordlist}")
            print(Fore.WHITE + f"[-] Hash-Type: {hashtype}")
            print(Fore.WHITE + f"[-] Hash: {password}")
            print(Fore.WHITE + f"[-] Word: {zxc}")
            print(Fore.WHITE + f"[-] Trying: {hashed}")
            print(Fore.WHITE + f"[-] Progress: {sayac}/{count}")
            sayac += 1
            sleep(0.000001)
            if(hashed == password):
                break
            os.system("cls")
        if(hashed == password):
            print(Fore.GREEN + "---------! Hash Cracked !----------")
            print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
            print(Fore.GREEN + f"[+] Password: {zxc}" + Style.RESET_ALL + Fore.RESET)
            sleep(3)
    #SHA224
    if(hashtype == "sha224"):
        for i in line:
            up_word = line[sayac]
            zxc = up_word.strip()
            hashed = hashlib.sha224(zxc.encode())
            hashed = hashed.hexdigest()
            print(Fore.WHITE + "[-] Attack Informations...")
            print(Fore.WHITE + f"[-] Wordlist: {wordlist}")
            print(Fore.WHITE + f"[-] Hash-Type: {hashtype}")
            print(Fore.WHITE + f"[-] Hash: {password}")
            print(Fore.WHITE + f"[-] Word: {zxc}")
            print(Fore.WHITE + f"[-] Trying: {hashed}")
            print(Fore.WHITE + f"[-] Progress: {sayac}/{count}")
            sayac += 1
            sleep(0.000001)
            if(hashed == password):
                break
            os.system("cls")
        if(hashed == password):
            print(Fore.GREEN + "---------! Hash Cracked !----------")
            print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
            print(Fore.GREEN + f"[+] Password: {zxc}" + Style.RESET_ALL + Fore.RESET)
            sleep(3)
    #BASE16
    if(hashtype == "base16"):
        msg_bytes = password.encode('ascii')
        base16_bytes = base64.b16decode(msg_bytes)
        base16_msg = base16_bytes.decode('ascii')
        print(Fore.WHITE + "[-] Attack Informations...")
        print(Fore.WHITE + f"[-] Encoding Type: {hashtype}")
        print(Fore.WHITE + f"[-] Encoded Text: {password}")
        print(Fore.GREEN + "---------! Base Decoded !----------")
        print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
        print(Fore.GREEN + f"[+] Password: {base16_msg}" + Style.RESET_ALL + Fore.RESET)
        sleep(3)
    #BASE32
    if(hashtype == "base32"):
        msg_bytes = password.encode('ascii')
        base32_bytes = base64.b32decode(msg_bytes)
        base32_msg = base32_bytes.decode('ascii')
        print(Fore.WHITE + "[-] Attack Informations...")
        print(Fore.WHITE + f"[-] Encoding Type: {hashtype}")
        print(Fore.WHITE + f"[-] Encoded Text: {password}")
        print(Fore.GREEN + "---------! Base Decoded !----------")
        print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
        print(Fore.GREEN + f"[+] Password: {base32_msg}" + Style.RESET_ALL + Fore.RESET)
        sleep(3)
    #BASE64
    if(hashtype == "base64"):
        msg_bytes = password.encode('ascii')
        base64_bytes = base64.b64decode(msg_bytes)
        base64_msg = base64_bytes.decode('ascii')
        print(Fore.WHITE + "[-] Attack Informations...")
        print(Fore.WHITE + f"[-] Encoding Type: {hashtype}")
        print(Fore.WHITE + f"[-] Encoded Text: {password}")
        print(Fore.GREEN + "---------! Base Decoded !----------")
        print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
        print(Fore.GREEN + f"[+] Password: {base64_msg}" + Style.RESET_ALL + Fore.RESET)
        sleep(3)
    #BASE85
    if(hashtype == "base85"):
        msg_bytes = password.encode('ascii')
        base85_bytes = base64.b85decode(msg_bytes)
        base85_msg = base85_bytes.decode('ascii')
        print(Fore.WHITE + "[-] Attack Informations...")
        print(Fore.WHITE + f"[-] Encoding Type: {hashtype}")
        print(Fore.WHITE + f"[-] Encoded Text: {password}")
        print(Fore.GREEN + "---------! Base Decoded !----------")
        print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
        print(Fore.GREEN + f"[+] Password: {base85_msg}" + Style.RESET_ALL + Fore.RESET)
        sleep(3)
    #ROT13
    if(hashtype == "rot13"):
        rot13e = codecs.decode(password, 'rot_13')
        print(Fore.WHITE + "[-] Attack Informations...")
        print(Fore.WHITE + f"[-] Encoding Type: {hashtype}")
        print(Fore.WHITE + f"[-] Encoded Text: {password}")
        print(Fore.GREEN + "---------! Rot Decoded !----------")
        print(Fore.YELLOW + f"[+] Hash-Type: {hashtype}")
        print(Fore.GREEN + f"[+] Password: {rot13e}" + Style.RESET_ALL + Fore.RESET)
        sleep(3)
        
#----------------------------------ENCODINGS---------------------------------------#

if(enc_dcd == "E" or enc_dcd == "e"):
    print("Supported Hash-Encoding Type: md5, sha1, sha256, sha512, sha384, sha224, base16, base32, base64, base85, rot13")
    etype = input("Hash-Encoding Type: ")
    anysalt = input("Salt ? (Y/N): ")
    if(anysalt == "Y" or anysalt == "y"):
        salt = input("enter salt: ")
    asd = str(input("Text: "))
    #MD5 Encoding
    if(etype == "md5"):
        if(anysalt == "N" or anysalt == "n"):
            ehash = hashlib.md5(asd.encode())
            ehash = ehash.hexdigest()
            print(Fore.BLUE + "---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Hashed Text: {ehash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            shash = hashlib.md5(salted.encode())
            shash = shash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Hashed Text: {shash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        
    #SHA256 Encoding
    if(etype == "sha256"):
        if(anysalt == "N" or anysalt == "n"):
            ehash = hashlib.sha256(asd.encode())
            ehash = ehash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Hashed Text: {ehash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            shash = hashlib.sha256(salted.encode())
            shash = shash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Hashed Text: {shash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #SHA512 Encoding
    if(etype == "sha512"):
        if(anysalt == "N" or anysalt == "n"):
            ehash = hashlib.sha512(asd.encode())
            ehash = ehash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Hashed Text: {ehash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            shash = hashlib.sha512(salted.encode())
            shash = shash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Hashed Text: {shash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #SHA1 Encoding
    if(etype == "sha1"):
        if(anysalt == "N" or anysalt == "n"):
            ehash = hashlib.sha1(asd.encode())
            ehash = ehash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Hashed Text: {ehash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            shash = hashlib.sha1(salted.encode())
            shash = shash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Hashed Text: {shash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #SHA224 Encoding
    if(etype == "sha224"):
        if(anysalt == "N" or anysalt == "n"):
            ehash = hashlib.sha224(asd.encode())
            ehash = ehash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Hashed Text: {ehash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            shash = hashlib.sha224(salted.encode())
            shash = shash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Hashed Text: {shash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #SHA384 Encoding
    if(etype == "sha384"):
        if(anysalt == "N" or anysalt == "n"):
            ehash = hashlib.sha384(asd.encode())
            ehash = ehash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Hashed Text: {ehash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            shash = hashlib.sha384(salted.encode())
            shash = shash.hexdigest()
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Hashed Text: {shash}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #BASE16 Encoding
    if(etype == "base16"):
        if(anysalt == "N" or anysalt == "n"):
            emsg_bytes = asd.encode('ascii')
            ebase16_bytes = base64.b16encode(emsg_bytes)
            ebase16_msg = ebase16_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase16_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            emsg_bytes = salted.encode('ascii')
            ebase16_bytes = base64.b16encode(emsg_bytes)
            ebase16_msg = ebase16_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase16_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #BASE32 Encoding
    if(etype == "base32"):
        if(anysalt == "N" or anysalt == "n"):
            emsg_bytes = asd.encode('ascii')
            ebase32_bytes = base64.b32encode(emsg_bytes)
            ebase32_msg = ebase32_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase32_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            emsg_bytes = salted.encode('ascii')
            ebase32_bytes = base64.b32encode(emsg_bytes)
            ebase32_msg = ebase32_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase32_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #BASE64 Encoding
    if(etype == "base64"):
        if(anysalt == "N" or anysalt == "n"):
            emsg_bytes = asd.encode('ascii')
            ebase64_bytes = base64.b64encode(emsg_bytes)
            ebase64_msg = ebase64_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase64_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            emsg_bytes = salted.encode('ascii')
            ebase64_bytes = base64.b64encode(emsg_bytes)
            ebase64_msg = ebase64_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase64_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #BASE85 Encoding
    if(etype == "base85"):
        if(anysalt == "N" or anysalt == "n"):
            emsg_bytes = asd.encode('ascii')
            ebase85_bytes = base64.b85encode(emsg_bytes)
            ebase85_msg = ebase85_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase85_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            emsg_bytes = salted.encode('ascii')
            ebase85_bytes = base64.b64encode(emsg_bytes)
            ebase85_msg = ebase85_bytes.decode('ascii')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Encoded Text: {ebase85_msg}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
    #ROT13 Encoding
    if(etype == "rot13"):
        if(anysalt == "N" or anysalt == "n"):
            dtext = codecs.encode(asd, 'rot_13')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: False")
            print(Fore.GREEN + f"[+] Encoded Text: {dtext}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)
        if(anysalt == "Y" or anysalt == "y"):
            salted = asd + salt
            dtext = codecs.encode(salted, 'rot_13')
            print("---------Encoding Result----------")
            print(f"[-] Text: {asd}")
            print(f"[-] Encoding Type: {etype}")
            print(Fore.YELLOW + "[-] Salted: True")
            print(Fore.YELLOW + f"[-] Salt: {salt}")
            print(Fore.GREEN + f"[+] Encoded Text: {dtext}" + Style.RESET_ALL + Fore.RESET )
            sleep(3)