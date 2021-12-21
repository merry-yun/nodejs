
import hashlib
import json
import math
import random
import requests
import re
from common import cookiesmodule
sess = requests.Session()
class AUTOSIGN():

    def sha1_encrypt(self, str):
        """
        使用sha1加密算法，返回str加密后的字符串
        """
        sha = hashlib.sha1(str.encode('utf-8'))
        encrypts = sha.hexdigest()
        return encrypts

    def hash_Param(self, params):
        """
        :param params: 传入参数params
        :return: 经过字母排序后的字符串
        """
        word_list = []
        middle = json.dumps(params, sort_keys=True)
        params = json.loads(middle)
        for key, value in params.items():
            if key == "api_key":
                continue
            word = '{}={}'.format(key, value)
            word_list.append(word)
        result = '&'.join(i for i in word_list)
        return result

    def get_mars_sid(self):
        encode_list = "0123456789abcdef"
        a = []
        for _ in range(32):
            index = math.ceil(1E8 * random.random()) % 16
            a.append(encode_list[index])
        result = ''.join(i for i in a)
        return result

    def get_secret(self, param):
        data = {
            "secret": "qyrohlf5sjazleru",
            "enString": {
                "70f71280d5d547b2a7bb370a529aeea1": "U2FsdGVkX197SM3Eh62XyjAwTXznW9DdALdNR1gKNsewAg3fzwA0x/+UQldlbi3oYBn8eFHgTtBUcGneYPCjIA==",
                "8cec5243ade04ed3a02c5972bcda0d3f": "U2FsdGVkX1+ZmG8rT/n9qDbrWBnK0K3G0gsoPo0N6/6qx8AklnZmXLyulj0KAy07ixFAu6oMKmOY0+VH3DjQ2Q==",
                "adf779847ac641dd9590ccc5674e25d2": "U2FsdGVkX1/VI+95aRUsSZCDB3rmMe2DPSUO+rSH7U/tlNnA5u9anTM3oHI+XgIeHWA5XDAo0Z19ddwzFeHFXA=="
                        }
                }
        word = data['enString'][param['api_key']]
        secret = data['secret']

    def get_mars_cid(self):
        url = "https://detail.vip.com/detail-1710614279-6917917216662086791.html"
        headers = {
            "Host": "detail.vip.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers"
        }
        response =sess.get(url, headers=headers)

        mars_cid = re.findall(r'mars_cid=(.*?);', response.headers['Set-Cookie']).pop()
        return mars_cid

    def main(self, param, api):
        sid = self.get_mars_sid()
        cid = self.get_mars_cid()
        param['mars_cid'] = cid
        hashParam = self.sha1_encrypt(self.hash_Param(param))
        secret = "ea6f62dad8ee40638832f3bd125f1a37"
        word = (api + hashParam + sid + cid + secret)
        sign = self.sha1_encrypt(word)
        return sign, sid, cid

if __name__ == "__main__":
    url = "https://mapi.vip.com/vips-mobile/rest/shopping/pc2/product/detail/v5"
    run = AUTOSIGN()
    api = "/vips-mobile/rest/shopping/pc2/product/detail/v5"
    param = {
        "app_name": "shop_pc",
        "app_version": "4.0",
        "warehouse": "VIP_NH",
        "fdc_area_id": "104104101",
        "client": "pc",
        "mobile_platform": 1,
        "province_id": 104104,
        "api_key": "70f71280d5d547b2a7bb370a529aeea1",
        "user_id": 466130329,
        "mars_cid": "1623135349504_16123904f05d38e641ee081723b085ac",
        "wap_consumer": "b",
        "productId": "6917917216662086791",
        "functions": "brand_store_info,newBrandLogo,hideOnlySize,extraDetailImages,sku_price,ui_settings",
        "kfVersion": 1,
        "highlightBgImgVer": 1,
        "is_get_TUV": "1",
        "commitmentVer": 2,
        "haitao_description_fields": "text",
        "supportSquare": 1,
        "longTitleVer": 2,
        "propsVer": 1,
    }
    sign, sid, cid = run.main(param, api)
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "OAuth api_sign=%s" % sign,
        "origin": "https://detail.vip.com",
        "referer": "https://detail.vip.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    cookies_str = "mars_cid=%s;  mars_sid=%s;" % (cid, sid)
    headers['Cookie'] = cookies_str
    response = requests.get(url, headers=headers, params=param)
    print(response.text)