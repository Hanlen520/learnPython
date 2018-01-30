#!/user/bin/env python
# -*- coding:utf-8 -*-

import sys
from Crypto.Cipher import AES
import base64
import os

PADDING = '\0'
# pkcs5padding
pad_it = lambda s: s+(16 - len(s)%16)*chr(16 - len(s) % 16)
# zeropadding
pad = lambda s: s+(16 - len(s)%16)*PADDING
# pkcs7padding,iso10126,ansix923

# 使用PyCrypto库进行ase加密
def decrypt_aes(cryptedStr):
    generator = AES.new('kaledaimall98765', AES.MODE_CBC, 'kaledaimall98765')
    cryptedStr = base64.b64decode(cryptedStr)
    recovery = generator.decrypt(cryptedStr)
    decryptedStr = recovery.rstrip(PADDING)
    return decryptedStr

if __name__ == '__main__':
    generator = AES.new('kaledaimall98765', AES.MODE_CBC, 'kaledaimall98765')
    crypt = generator.encrypt(pad_it('456456'))
    cryptedStr = base64.b64encode(crypt)
    print cryptedStr

    print decrypt_aes(cryptedStr)

