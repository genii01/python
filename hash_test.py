import hashlib

secret = "this is the password or document text"

bsecret = secret.encode()

m = hashlib.md5()
m.update(bsecret)
print(m.digest())
