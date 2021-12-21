
import requests

url = "http://172.18.11.249:5050/toutiaoSign"
data = {
    "url": "https://www.toutiao.com",
    "cookie": 'gf_part_97293=0; x-jupiter-uuid=16319454484428750; MONITOR_WEB_ID=9ba74e28-ea5b-41b8-b41e-72d2e99dd960; ttcid=0b8c53b99c1d4550a783233a33b4b0c533; gf_part_97293=0; x-jupiter-uuid=16319454495288842; passport_csrf_token_default=14c7544cd7ced4f66f4ccbed78b9275e; passport_csrf_token=14c7544cd7ced4f66f4ccbed78b9275e; s_v_web_id=verify_c0d76f78482943851689169265d8b604; MONITOR_DEVICE_ID=9ae3b781-bbbc-4e6a-8ae3-4a6e44e98ba6; sso=https://fxg.jinritemai.com/ffa/mshop/subaccount/apply; PHPSESSID=ece7faf98a78c711a79b42a40d17c5b6; PHPSESSID_SS=ece7faf98a78c711a79b42a40d17c5b6; LUOPAN_DT=session_7009151280136421673; Hm_lvt_45173f3eae0174bc5b02a4973fe5a872=1631945449,1631945527,1631945534; Hm_lpvt_45173f3eae0174bc5b02a4973fe5a872=1631945534; tt_scid=g-dF4mx95LTNGft08dSMAY0rtYqnm3ORIwitwae1gKujClk-SCU9EWcBqKa9XcNZ8865'
}

response = requests.post(url, json=data)
print(response.text)