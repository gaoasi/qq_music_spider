import time

import execjs
import requests
import json

ts = int(time.time()*1000)
cookies = {
    'pgv_pvid': '7579412345',
    'fqm_pvqid': '11291234-a8a1-4b17-8e75-a6d027fddc90',
    'ts_uid': '1747659299',
    'ts_refer': 'www.google.com/',
    'fqm_sessionid': '377a86d8-b705-441c-9109-6aee416067f8',
    'pgv_info': 'ssid=s1706854146',
    'login_type': '2',
    'psrf_qqaccess_token': '',
    'qm_keyst': 'W_X_63B0aE92i00Wh0RPj-D5IoE1uSAIoS7VvKPSg6arI9UpC0CAWu8rFhfFKBkY_Jb0msRSs2O8g4_zPz9s41FACO3AI',
    'wxuin': '1152921504896177477',
    'qm_keyst': 'W_X_63B0aE92i00Wh0RPj-D5IoE1uSAIoS7VvKPSg6arI9UpC0CAWu8rFhfFKBkY_Jb0msRSs2O8g4_zPz9s41FACO3AI',
    'wxuin': '1152921504896177477',
    'psrf_qqopenid': '',
    'wxrefresh_token': '82_WN0rCvR5OKyiMuBk6eagJh9Sx-lStcbp5vvAhUvCBve8rMCyQcivy4Xp2nrhQOmRlKDDrR3QnOtvN0byl--hoFOIYltddfvsZBNFJP7ZlR8',
    'wxopenid': 'opCFJw9GTDxYWC1ND-I4teOYImEk',
    'tmeLoginType': '1',
    'qqmusic_key': 'W_X_63B0aE92i00Wh0RPj-D5IoE1uSAIoS7VvKPSg6arI9UpC0CAWu8rFhfFKBkY_Jb0msRSs2O8g4_zPz9s41FACO3AI',
    'wxunionid': 'oqFLxsvo5OuZNInLnNI55-GLetUM',
    'psrf_qqunionid': '',
    'euin': 'oK6kowEAoK4z7ecq7w6l7ivl7z**',
    'psrf_qqrefresh_token': '',
    'ts_last': 'y.qq.com/n/ryqq/search',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'pgv_pvid=7579412345; fqm_pvqid=11291234-a8a1-4b17-8e75-a6d027fddc90; ts_uid=1747659299; ts_refer=www.google.com/; fqm_sessionid=377a86d8-b705-441c-9109-6aee416067f8; pgv_info=ssid=s1706854146; login_type=2; psrf_qqaccess_token=; qm_keyst=W_X_63B0aE92i00Wh0RPj-D5IoE1uSAIoS7VvKPSg6arI9UpC0CAWu8rFhfFKBkY_Jb0msRSs2O8g4_zPz9s41FACO3AI; wxuin=1152921504896177477; qm_keyst=W_X_63B0aE92i00Wh0RPj-D5IoE1uSAIoS7VvKPSg6arI9UpC0CAWu8rFhfFKBkY_Jb0msRSs2O8g4_zPz9s41FACO3AI; wxuin=1152921504896177477; psrf_qqopenid=; wxrefresh_token=82_WN0rCvR5OKyiMuBk6eagJh9Sx-lStcbp5vvAhUvCBve8rMCyQcivy4Xp2nrhQOmRlKDDrR3QnOtvN0byl--hoFOIYltddfvsZBNFJP7ZlR8; wxopenid=opCFJw9GTDxYWC1ND-I4teOYImEk; tmeLoginType=1; qqmusic_key=W_X_63B0aE92i00Wh0RPj-D5IoE1uSAIoS7VvKPSg6arI9UpC0CAWu8rFhfFKBkY_Jb0msRSs2O8g4_zPz9s41FACO3AI; wxunionid=oqFLxsvo5OuZNInLnNI55-GLetUM; psrf_qqunionid=; euin=oK6kowEAoK4z7ecq7w6l7ivl7z**; psrf_qqrefresh_token=; ts_last=y.qq.com/n/ryqq/search',
    'origin': 'https://y.qq.com',
    'priority': 'u=1, i',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
js_code = open('qq_music_get_download_url.js').read()
data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921504896177477","g_tk_new_20200303":600551515,"g_tk":600551515},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"65358286915851067","search_type":0,"query":"林俊杰","page_num":1,"num_per_page":20}},"req_2":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"70193599752393532","search_type":0,"query":"林俊杰","page_num":1,"num_per_page":20}}}'
sign = execjs.compile(js_code).call('get_data')
# params = {
#     '_': ts,
#     'sign': sign,
# }
#
#
#
# response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies, headers=headers, data=data)
#
# print(json.dumps(response.json(), ensure_ascii=False, indent=4))
print(sign)