const FormData = require('form-data');
document = {
    cookie: '"cookie"',
}
data = {
    format: "jsonp",
    url: "//y.qq.com/download/download.js",
    data: {},
    jsonpCallback: "MusicJsonCallback"
}
A = function (e) {
    return "[object Object]" === Object.prototype.toString.call(e)
}
x = function (e) {
    return A(e) && null !== e && e !== e.window && Object.getPrototypeOf(e) === Object.prototype
}
T = function (e) {
    for (var t, n = !1, r = arguments.length, i = new Array(r > 1 ? r - 1 : 0), o = 1; o < r; o++)
        i[o - 1] = arguments[o];
    "boolean" === typeof e ? (n = e,
        t = i.shift()) : t = e;
    var a = function e(t, n, r) {
        Object.keys(n).forEach((function (i) {
                var o = n[i];
                r && x(o) || Array.isArray(o) ? (x(o) && !x(t[i]) && (t[i] = {}),
                Array.isArray(n[i]) && !Array.isArray(t[i]) && (t[i] = []),
                    e(t[i], n[i], r)) : void 0 !== o && (t[i] = o)
            }
        ))
    };
    return i.forEach((function (e) {
            a(t, e, n)
        }
    )),
        t
}
K = {
    cv: 4747474,
    ct: 24,
    format: "json",
    inCharset: "utf-8",
    outCharset: "utf-8",
    notice: 0,
    platform: "yqq.json",
    needNewCode: 1
}
l = function (e) {
    var t = null;
    if (true) {
        var n = document.cookie.match(RegExp("(^|;\\s*)" + e + "=([^;]*)(;|$)"));
        t = n ? decodeURIComponent(n[2]) : ""
    } else
        t = (null === i || void 0 === i ? void 0 : i.cookies[e]) || "";
    return function (e) {
        if (!e)
            return e;
        for (; e !== decodeURIComponent(e);)
            e = decodeURIComponent(e);
        var t = ["<", ">", "'", '"', "%3c", "%3e", "%27", "%22", "%253c", "%253e", "%2527", "%2522"]
            ,
            n = ["&#x3c;", "&#x3e;", "&#x27;", "&#x22;", "%26%23x3c%3B", "%26%23x3e%3B", "%26%23x27%3B", "%26%23x22%3B", "%2526%2523x3c%253B", "%2526%2523x3e%253B", "%2526%2523x27%253B", "%2526%2523x22%253B"];
        return t.forEach((function (r, i) {
                e = e.replace(new RegExp(t[i], "gi"), n[i])
            }
        )),
            e
    }(t)
}

d = function () {
    return !!l("wxopenid")
}

f = function (e) {
    var t, n = 5381;
    if (t = e ? l("qqmusic_key") || l("p_skey") || l("skey") || l("p_lskey") || l("lskey") : l("skey") || l("qqmusic_key"))
        for (var r = 0, i = t.length; r < i; ++r)
            n += (n << 5) + t.charCodeAt(r);
    return 2147483647 & n
}

h = function () {
    var e = 0;
    return 0 === (e = (e = d() ? l("wxuin") : l("uin")) || l("p_uin")).indexOf("o") && (e = e.substring(1, e.length)),
        /^\d+$/.test(e) ? e.length < 14 && (e = parseInt(e, 10)) : e = 0,
        e
}

function w(e) {
    var t = {
        data: K,
        time: 1e4,
        withCredentials: !0,
        cache: !1
    };
    t.data.uin = h() || 0,
        t.data.g_tk_new_20200303 = f(!0),
        t.data.g_tk = f(),
    e.postType && (t.data = {
        comm: t.data
    }),
    e.data && "string" === typeof e.data && (e.data = C(e.data)),
        true && e.data instanceof FormData ? t.data = e.data : t.data = T(!0, {}, t.data, e.data),
        delete e.data;
    var n = Object.assign(t, e);

    return n
}

param = w(data)

function get_params(song) {
    var a = (new Date).getUTCMilliseconds(),
        guid = String(Math.round(2147483647 * Math.random()) * a % 1e10)
        file_name = "RS02".concat((null === (c = song.vs) || void 0 === c ? void 0 : c[0]) || (null === (u = song.file) || void 0 === u ? void 0 : u.media_mid), ".mp3")

        p = {
            "comm": param,
            "req_1": {
                "module": "userInfo.VipQueryServer",
                "method": "SRFVipQuery_V2",
                "param": {"uin_list": [param.data.uin]}
            },
            "req_2": {
                "module": "userInfo.BaseUserInfoServer",
                "method": "get_user_baseinfo_v2",
                "param": {"vec_uin": [param.data.uin]}
            },
            "req_3": {"module": "music.lvz.VipIconUiShowSvr", "method": "GetVipIconUiV2", "param": {"PID": 3}},
            "req_4": {
                "module": "music.musicasset.SongFavRead",
                "method": "IsSongFanByMid",
                "param": {"v_songMid": [song['mid']]}
            },
            "req_5": {
                "module": "music.musichallSong.PlayLyricInfo",
                "method": "GetPlayLyricInfo",
                "param": {"songMID": song['mid'], "songID": song['id']}
            },
            "req_6": {
                "method": "GetCommentCount",
                "module": "music.globalComment.GlobalCommentRead",
                "param": {"request_list": [{"biz_type": 1, "biz_id": song['id'], "biz_sub_type": song['type']}]}
            },
            "req_7": {
                "module": "music.musichallAlbum.AlbumInfoServer",
                "method": "GetAlbumDetail",
                "param": {"albumMid": song['album']['mid']}
            },
            "req_8": {
                "module": "music.vkey.GetVkey",
                "method": "GetUrl",
                "param": {
                    "guid": guid,
                    "songmid": [song['mid']],
                    "songtype": [song['type']],
                    "uin": param.data.uin,
                    "loginflag": 1,
                    "platform": "20",
                    "filename": [file_name]
                }
            }
        }
    return JSON.stringify(p)
}

var urls = {}
function get_url(e){
    if (e && e.midurlinfo) {
        debugger
        var n = e.thirdip && e.thirdip[0] ? e.thirdip[0] : "https://ws6.stream.qqmusic.qq.com/";
        e.midurlinfo.forEach((function (e, a) {
                if (e) {
                    var r = e.purl;
                    r && !/^https?:\/\//i.test(r) && (r = n + r),
                        urls[e.songmid] = r
                }
            }
        ))
    }
}

function get_data(data){
    debugger
    data.forEach((function (t) { get_url(t.data) }))
    return urls
}
