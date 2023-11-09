from hashlib import md5

sKey = "yzbqklnj"

for i in range (10000000000000000):
    hashCode = md5((sKey + str(i)).encode()).hexdigest()
    if hashCode[:6] == '000000':
        print(i)
        break