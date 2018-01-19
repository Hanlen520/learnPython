#!/user/bin/env python
# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
import base64,json
import hashlib

PADDING = '\0'
# pkcs5padding
pad_it = lambda s: s+(16 - len(s)%16)*chr(16 - len(s) % 16)

def encrypt(pswStr):
    generator = AES.new('kaledaimall98765', AES.MODE_CBC, 'kaledaimall98765')
    crypt = generator.encrypt(pad_it(pswStr))
    cryptedStr = base64.b64encode(crypt)
    return cryptedStr

def md5(str):
    md5_pwd = hashlib.md5()
    # 158 9544b351297a40b18cb5252eb7cdedd60 0876019
    md5_pwd.update(str)
    print u"sign加密后：",md5_pwd.hexdigest()
    return md5_pwd.hexdigest()

if __name__ == '__main__':
    cellphone = '15800876020'
    psw = '456456'
    print encrypt(psw)

    md5(cellphone[:3] + "9544b351297a40b18cb5252eb7cdedd6" + cellphone[3:])