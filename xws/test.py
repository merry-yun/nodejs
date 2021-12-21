
import execjs
file_path = "./encrypt_xws.js"

def get_info(t, e, a, i):
    """
    :param t:
    :param e:
    :param a:
    :param i:
    :return:
    """
    func = execjs.compile(r"const INFO = require('%s');" % file_path)
    info = func.call('INFO', t, e, a, i)
    return info

if __name__ == "__main__":
    t = 50023722
    e = {
        "tradeIndex": [124313]
    }
    a = "小奥汀旗舰店"
    i = {
        "mainNick": "小奥汀旗舰店",
        "mainUserId": "2429621953"
    }
    info = get_info(t, e, a, i)
    data = {
        "info": info
    }
    print(data)