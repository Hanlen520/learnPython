#!/user/bin/env python
# -*- coding:utf-8 -*-
import hashlib

# 6ecd4afcd41dcee0dc0a2fde717c5309
# 3337c37cae894e469446392ff7457279
# 9ad0fbcaacd2a14c32726bee2f5b6a95fb6990ac61412a4f
# 9d7760ec8eabd41be6684f7a2e22d082
def getcellphone(cellphone):
    m2 = hashlib.md5()
    # m2.update(cellphone)
    m2.update('123456')
    m2.update('3337c37cae894e469446392ff7457279')
    # print hashlib.sha256(cellphone).hexdigest()
    # print hashlib.sha384(cellphone).hexdigest()
    # print hashlib.sha512(cellphone).hexdigest()
    m2.hexdigest
    print m2.hexdigest()

def test():
    md5_pwd = hashlib.md5()
    # 158 9544b351297a40b18cb5252eb7cdedd6 00876019
    md5_pwd.update('13572489850')
    print md5_pwd.hexdigest()
    # print hashlib.sha1('1234562ba9cc2679881b09dc6d052823ba37d5').hexdigest()


if __name__ == '__main__':
    # getcellphone('13572489850')
    test()