import json
import time

import execjs
import requests

ts = int(time.time()*1000)
cookie = 'pgv_pvid=7579412345; fqm_pvqid=11291234-a8a1-4b17-8e75-a6d027fddc90; ts_uid=1747659299; ts_refer=www.google.com/; fqm_sessionid=377a86d8-b705-441c-9109-6aee416067f8; pgv_info=ssid=s1706854146; login_type=2; ts_last=y.qq.com/n/ryqq/player; wxuin=1152921504896177477; tmeLoginType=1; psrf_qqunionid=; wxrefresh_token=82_vB9qfVTWsbvejclsAtP4mbOfFc8KMGZEoBycCIzwrwhzRyrc67eyf9MB_T32i4oHegW-Ay50iRadpXOYk1NIrgg8i1--ETMsQ7sVTX9hqEw; psrf_qqrefresh_token=; psrf_qqaccess_token=; qqmusic_key=W_X_63B0aUDdS_wOxviH5U2NDQ5N4n3_WhZfgB3er6fHOKDtR64UtrFQvFZ1MoaMrLfXYj-tJAtocZQg9UiCU7XM7Gd1bwAI; euin=oK6kowEAoK4z7ecq7w6l7ivl7z**; wxopenid=opCFJw9GTDxYWC1ND-I4teOYImEk; wxunionid=oqFLxsvo5OuZNInLnNI55-GLetUM; psrf_qqopenid=; qm_keyst=W_X_63B0aUDdS_wOxviH5U2NDQ5N4n3_WhZfgB3er6fHOKDtR64UtrFQvFZ1MoaMrLfXYj-tJAtocZQg9UiCU7XM7Gd1bwAI; wxuin=1152921504896177477; qm_keyst=W_X_63B0aUDdS_wOxviH5U2NDQ5N4n3_WhZfgB3er6fHOKDtR64UtrFQvFZ1MoaMrLfXYj-tJAtocZQg9UiCU7XM7Gd1bwAI'
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': cookie,
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

js_code = execjs.compile(open('webpack.js').read().replace('"cookies"',cookie))
item_key = '周杰伦'
num_per_page = 5
search_param = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921504896177477","g_tk_new_20200303":600551515,"g_tk":600551515},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"65358286915851067","search_type":0,"query":"'+item_key+'","page_num":1,"num_per_page":'+str(num_per_page)+'}},"req_2":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"70193599752393532","search_type":0,"query":"'+item_key+'","page_num":1,"num_per_page":'+str(num_per_page)+'}}}'
sign = js_code.call('getSign', search_param)
params = {
    '_': ts,
    'sign': sign,
}

response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params,  headers=headers, data=search_param)

res_songs = response.json()
songs = res_songs['req_1']['data']['body']['song']['list']
songs_info = []
song_dic = {}
song_params_code = execjs.compile(open("get_song_param.js").read().replace('"cookie"',cookie))
for song in songs:
    song_param = song_params_code.call('get_params', song)
    song_dic[song['mid']] = {}
    song_dic[song['mid']]['name'] = song['name']
    song_dic[song['mid']]['singer'] = song['singer'][0]['name']
    song_sign = js_code.call('getSign', song_param)
    song_ts = int(time.time()*1000)
    song_req_params = {
        '_': song_ts,
        'sign': song_sign,
    }
    song_res= requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=song_req_params,  headers=headers, data=song_param)

    songs_info.append(song_res.json()['req_8'])

urls = song_params_code.call('get_data', songs_info)
for key in song_dic:
    song_dic[key]['url'] = urls[key]

print(json.dumps(song_dic,indent=4,ensure_ascii=False))
