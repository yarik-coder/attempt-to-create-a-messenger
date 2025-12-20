import rsa
from stegano import lsb

(pubkey, privkey) = rsa.newkeys(512)
message = input()
message = message.encode()

# шифруем
crypto = rsa.encrypt(message, pubkey)
print(crypto)
print("\n")
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message.decode())
a = open("save_cheto.txt", "w", encoding="UTF-8")
a.write(str(crypto)[2:-1])
a.close()
pub_key_data = pubkey.save_pkcs1().decode('utf-8')
secret_img = lsb.hide("stonks.png", pub_key_data)
secret_img.save("result_with_key.png")