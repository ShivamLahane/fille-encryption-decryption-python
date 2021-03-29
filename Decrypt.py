from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# opening the encrypted file
with open('file.txt', 'rb') as enc_file:
    encrypted = enc_file.read()

fernet = Fernet(key)

# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('file.txt', 'wb') as dec_file:
    dec_file.write(decrypted)