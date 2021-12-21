
import requests

headers = {
    'authority': 'mar.vip.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '^\\^',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://defend.vip.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'vipshop_passport_src=https^%^3A^%^2F^%^2Fe.vip.com^%^2Fmain.html^%^3Fclchash^%^3D1; mars_pid=0; mars_sid=b281e46d146b664decfd15d07dc7e28c; visit_id=1F5653531B869E0C9D828BFC861142C3; _jzqco=^%^7C^%^7C^%^7C^%^7C^%^7C1.1298891106.1626836834371.1626836834371.1626836834371.1626836834371.1626836834371.0.0.0.1.1; pg_session_no=1; vip_tracker_source_from=; mars_cid=1626836834331_7c1ba0a81f6973b2e42a62223f42264f',
    'sec-fetch-user': '?1',
    'origin': 'https://defend.vip.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    'Referer': '',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'x-requested-with': 'XMLHttpRequest',
    'authorization': 'OAuth api_sign=01b290bf200f0b5ab50ae25a421da659545eef20',
    'content-type': 'text/plain;charset=UTF-8',
}

params = (
    ('r', 'form.index'),
    ('sign', 'efc405c3f78aa179231df8ba07d67226'),
    ('challengeId', '31ea5d84-d0c5-458e-81ce-eb8d8562556c'),
    ('callback', 'https^%^3A^%^2F^%^2Fpassport.vip.com^%^2Flogin^%^2FcheckChallengeLogin'),
    ('challengeWayName', 'VerifyBoundPhone'),
    ('page', 'one'),
)

data = {
  'api_key': '70f71280d5d547b2a7bb370a529aeea1',
  'pc_eversion': '1',
  'skey': '3c5ad16dbc06cd16ae1fd3344d87f16b',
  'pc_edata': 'w^%^2FtGg7nKG13Rj4pNvdheEtwCbiaRkBsuh6be0LiFA8fQ4bO56oWqWiwtPZbyX2j68Bcr5vlRm^%^2BwLwqvQiCVHqoTl010MOfDx^%^2BaEPLXLSFzkuidd3HfUemwZM3PRCEuICGM^%^2F0ohJziYs^%^2FR^%^2FUPj^%^2BHQvSS2N4coa8gFpEpZcFUil8Op29iyouQTeHYNSqdzeEvQEVUGjrudrzKnvF97VW3sG^%^2BobSEXG9^%^2BHd5KlPZrb82WR4QcdedMz91kKhQF8IZAQG',
  '^{^\\^session_id^\\^:^\\^-99^\\^,^\\^mars_cid^\\^:^\\^^\\^,^\\^user_id^\\^:^\\^^\\^,^\\^app_name^\\^:^\\^pc^\\^,^\\^app_type^\\^:^\\^web^\\^,^\\^app_platform^\\^:^\\^pc^\\^,^\\^monitor_name^\\^:^\\^m_api^\\^,^\\^monitor_data^\\^:^{^\\^api_name^\\^:^\\^passport.vip.com/login/postLogin^\\^,^\\^request_time^\\^:1626836903166,^\\^response_time^\\^:1626836903351,^\\^status^\\^:200,^\\^service_ip^\\^:^\\^-99^\\^,^\\^request_url^\\^:^\\^https://passport.vip.com/login/postLogin^\\^,^\\^dns_time^\\^:^\\^-99^\\^,^\\^rpc_status^\\^:^\\^-99^\\^,^\\^cpu_support^\\^:^\\^-99^\\^,^\\^enable_routing^\\^:^\\^-99^\\^,^\\^domain^\\^:^\\^passport.vip.com^\\^,^\\^disable_domain^\\^:^\\^-99^\\^,^\\^network_mark^\\^:0,^\\^service_code^\\^:^\\^-99^\\^,^\\^original_code^\\^:^\\^-99^\\^,^\\^msg^\\^:^\\^-99^\\^,^\\^detail_msg^\\^:^\\^-99^\\^,^\\^retry_times^\\^:^\\^-99^\\^,^\\^browser^\\^:^\\^Chrome_91^\\^,^\\^page_url^\\^:^\\^https://passport.vip.com/login?whereFrom': 'vipotd',
  'src': 'https^%^3A^%^2F^%^2Fe.vip.com^%^2Fmain.html^%^3Fclchash^%^3D1^\\^,^\\^page_name^\\^:^\\^passport.vip.com/login^\\^,^\\^user_agent^\\^:^\\^Mozilla/5.0'
}

response = requests.post('https://defend.vip.com/index/pc/', headers=headers, params=params, data=data)
print(response.text)