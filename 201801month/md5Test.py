#!/user/bin/env python
# -*- coding:utf-8 -*-
import hashlib

# 6ecd4afcd41dcee0dc0a2fde717c5309
# 3337c37cae894e469446392ff7457279
# 9ad0fbcaacd2a14c32726bee2f5b6a95fb6990ac61412a4f
def getcellphone(cellphone):
    m2 = hashlib.md5()
    # m2.update(cellphone)
    m2.update('123456')
    m2.update('3337c37cae894e469446392ff7457279')
    print hashlib.sha256(cellphone).hexdigest()
    print hashlib.sha384(cellphone).hexdigest()
    print hashlib.sha512(cellphone).hexdigest()
    return m2.hexdigest()

if __name__ == '__main__':
    print getcellphone('13572489850')