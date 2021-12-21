# -*- coding:utf-8 -*-
import base64
from Crypto.Cipher import AES


class EncryptDate:
    def __init__(self, key):
        self.key = key  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def pad(self, text):
        """
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        """
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)

if __name__ == '__main__':
    key = "5a64b0170ee322b747a045ba"
    msg = 'i9qCDXS2tnvzM2Gg2fminIYVFngkBAXHgA4jDzbbyiu2WRHfaIKEaDisrCIKJsi3hk9D1OcUmT2HY5/HqSv+NlVa/z4U3jE50xxLZpWBAMmqMk+79lNEW+rVGD9ZIWs8dA8aEeKbP9Zo6fYA3L9OKECVbmwZPyKIS4d681ApYIul0EIDPFsYOP/aD9nGSY9c5aVYztjZaQYFuVXxJoj36XXomrcDqLjexYmRlS2blxKk2jTt6nRWkNykCm3qLgq6f6uU0UWywA96+1cq1oFAZPMVAdnDaI/VONeA0Zf3Wyy42fbaB25wK76nF6tBX38XNkamt2fGQi3/pGmkkeYPLAeELt5DRMgRE2dsCLxJPPh76qiB2RB5uE20BQ3w407P7YuJXCEwIlcv4ti7dHzUYMCe6ld9Csrm/OrtbKHVjWQjW6FM4Jp09+m0ILBXSTCZb5SjECHVHMytUCCthhSCH9calxzpKaCXWGDpC4mqA/BVxuTf2d3wCHulcH90V2FxGXGni7VSZm29E0Zdf//S0YGnMRTno8JXQzblGNcls5pHdpLurQHHit2EMQMY4Wv13xdFbJ/5GPKQ8SJd5gzWJkOIaICIno3mw+AuqPQUBRUCHtulU//k6S3yyyaBQjmZRUc2JHWH9xqw9Z3c49RG/KNWVHLGCB1nIp8dDxZXGy0BiHHxL4gVwSNlpUeV48SgLnkZ9msYBkh8G4Q/RGT1k7xKtWQyxOcJzl/LhHoHDjYilcpZGc9W1A8cRfPUJbFsIHIbw+MF6kYDVdD0SbBy8Wuq79zEgnKXc6E1e47U9N3T7NBmuG5J1igl+i94ymZdYvdzAWbzlly0ubyUH1o5uYutBcESB6NkPO09ImdGVuHYMmJkpBlk7RfrfKbFGYNW0ZunWn4amzTBC7ALwHhoLZCyzbzWa0AQZJS6tSsCNWP6W296Uid/bF2VAZP0buUe'
    eg = EncryptDate(key.encode('utf-8'))
    res = eg.decrypt(msg)
    # res = eg.encrypt("中文测试！")
    print(res)