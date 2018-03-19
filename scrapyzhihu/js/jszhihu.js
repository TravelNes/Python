function a(e, t, n) {
    var r, o, a, i, s, u, c, l, v, b = 0, g = [], _ = 0, w = !1, E = [], O = [], k = !1, T = !1;
    if (n = n || {},
    r = n.encoding || "UTF8",
    v = n.numRounds || 1,
    a = y(t, r),
    v !== parseInt(v, 10) || 1 > v)
        throw Error("numRounds must a integer >= 1");
    if ("SHA-1" === e)
        s = 512,
        u = B,
        c = U,
        i = 160,
        l = function(e) {
            return e.slice()
        }
        ;
    else if (0 === e.lastIndexOf("SHA-", 0))
        if (u = function(t, n) {
            return q(t, n, e)
        }
        ,
        c = function(t, n, r, o) {
            var a, i;
            if ("SHA-224" === e || "SHA-256" === e)
                a = 15 + (n + 65 >>> 9 << 4),
                i = 16;
            else {
                if ("SHA-384" !== e && "SHA-512" !== e)
                    throw Error("Unexpected error in SHA-2 implementation");
                a = 31 + (n + 129 >>> 10 << 5),
                i = 32
            }
            for (; t.length <= a; )
                t.push(0);
            for (t[n >>> 5] |= 128 << 24 - n % 32,
            n += r,
            t[a] = 4294967295 & n,
            t[a - 1] = n / 4294967296 | 0,
            r = t.length,
            n = 0; n < r; n += i)
                o = q(t.slice(n, n + i), o, e);
            if ("SHA-224" === e)
                t = [o[0], o[1], o[2], o[3], o[4], o[5], o[6]];
            else if ("SHA-256" === e)
                t = o;
            else if ("SHA-384" === e)
                t = [o[0].a, o[0].b, o[1].a, o[1].b, o[2].a, o[2].b, o[3].a, o[3].b, o[4].a, o[4].b, o[5].a, o[5].b];
            else {
                if ("SHA-512" !== e)
                    throw Error("Unexpected error in SHA-2 implementation");
                t = [o[0].a, o[0].b, o[1].a, o[1].b, o[2].a, o[2].b, o[3].a, o[3].b, o[4].a, o[4].b, o[5].a, o[5].b, o[6].a, o[6].b, o[7].a, o[7].b]
            }
            return t
        }
        ,
        l = function(e) {
            return e.slice()
        }
        ,
        "SHA-224" === e)
            s = 512,
            i = 224;
        else if ("SHA-256" === e)
            s = 512,
            i = 256;
        else if ("SHA-384" === e)
            s = 1024,
            i = 384;
        else {
            if ("SHA-512" !== e)
                throw Error("Chosen SHA variant is not supported");
            s = 1024,
            i = 512
        }
    else {
        if (0 !== e.lastIndexOf("SHA3-", 0) && 0 !== e.lastIndexOf("SHAKE", 0))
            throw Error("Chosen SHA variant is not supported");
        var S = 6;
        if (u = V,
        l = function(e) {
            var t, n = [];
            for (t = 0; 5 > t; t += 1)
                n[t] = e[t].slice();
            return n
        }
        ,
        "SHA3-224" === e)
            s = 1152,
            i = 224;
        else if ("SHA3-256" === e)
            s = 1088,
            i = 256;
        else if ("SHA3-384" === e)
            s = 832,
            i = 384;
        else if ("SHA3-512" === e)
            s = 576,
            i = 512;
        else if ("SHAKE128" === e)
            s = 1344,
            i = -1,
            S = 31,
            T = !0;
        else {
            if ("SHAKE256" !== e)
                throw Error("Chosen SHA variant is not supported");
            s = 1088,
            i = -1,
            S = 31,
            T = !0
        }
        c = function(e, t, n, r, o) {
            n = s;
            var a, i = S, u = [], c = n >>> 5, l = 0, f = t >>> 5;
            for (a = 0; a < f && t >= n; a += c)
                r = V(e.slice(a, a + c), r),
                t -= n;
            for (e = e.slice(a),
            t %= n; e.length < c; )
                e.push(0);
            for (a = t >>> 3,
            e[a >> 2] ^= i << 24 - a % 4 * 8,
            e[c - 1] ^= 128,
            r = V(e, r); 32 * u.length < o && (e = r[l % 5][l / 5 | 0],
            u.push((255 & e.b) << 24 | (65280 & e.b) << 8 | (16711680 & e.b) >> 8 | e.b >>> 24),
            !(32 * u.length >= o)); )
                u.push((255 & e.a) << 24 | (65280 & e.a) << 8 | (16711680 & e.a) >> 8 | e.a >>> 24),
                0 == 64 * (l += 1) % n && V(null, r);
            return u
        }
    }
    o = Y(e),
    this.setHMACKey = function(t, n, a) {
        var l;
        if (!0 === w)
            throw Error("HMAC key already set");
        if (!0 === k)
            throw Error("Cannot set HMAC key after calling update");
        if (!0 === T)
            throw Error("SHAKE is not supported for HMAC");
        if (r = (a || {}).encoding || "UTF8",
        n = y(n, r)(t),
        t = n.binLen,
        n = n.value,
        l = s >>> 3,
        a = l / 4 - 1,
        l < t / 8) {
            for (n = c(n, t, 0, Y(e), i); n.length <= a; )
                n.push(0);
            n[a] &= 4294967040
        } else if (l > t / 8) {
            for (; n.length <= a; )
                n.push(0);
            n[a] &= 4294967040
        }
        for (t = 0; t <= a; t += 1)
            E[t] = 909522486 ^ n[t],
            O[t] = 1549556828 ^ n[t];
        o = u(E, o),
        b = s,
        w = !0
    }
    ,
    this.update = function(e) {
        var t, n, r, i = 0, c = s >>> 5;
        for (t = a(e, g, _),
        e = t.binLen,
        n = t.value,
        t = e >>> 5,
        r = 0; r < t; r += c)
            i + s <= e && (o = u(n.slice(r, r + c), o),
            i += s);
        b += i,
        g = n.slice(i >>> 5),
        _ = e % s,
        k = !0
    }
    ,
    this.getHash = function(t, n) {
        var r, a, s, u;
        if (!0 === w)
            throw Error("Cannot call getHash after setting HMAC key");
        if (s = m(n),
        !0 === T) {
            if (-1 === s.shakeLen)
                throw Error("shakeLen must be specified in options");
            i = s.shakeLen
        }
        switch (t) {
        case "HEX":
            r = function(e) {
                return f(e, i, s)
            }
            ;
            break;
        case "B64":
            r = function(e) {
                return d(e, i, s)
            }
            ;
            break;
        case "BYTES":
            r = function(e) {
                return p(e, i)
            }
            ;
            break;
        case "ARRAYBUFFER":
            try {
                a = new ArrayBuffer(0)
            } catch (e) {
                throw Error("ARRAYBUFFER not supported by this environment")
            }
            r = function(e) {
                return h(e, i)
            }
            ;
            break;
        default:
            throw Error("format must be HEX, B64, BYTES, or ARRAYBUFFER")
        }
        for (u = c(g.slice(), _, b, l(o), i),
        a = 1; a < v; a += 1)
            !0 === T && 0 != i % 32 && (u[u.length - 1] &= 4294967040 << 24 - i % 32),
            u = c(u, i, 0, Y(e), i);
        return r(u)
    }
    ,
    this.getHMAC = function(t, n) {
        var r, a, y, v;
        if (!1 === w)
            throw Error("Cannot call getHMAC without first setting HMAC key");
        switch (y = m(n),
        t) {
        case "HEX":
            r = function(e) {
                return f(e, i, y)
            }
            ;
            break;
        case "B64":
            r = function(e) {
                return d(e, i, y)
            }
            ;
            break;
        case "BYTES":
            r = function(e) {
                return p(e, i)
            }
            ;
            break;
        case "ARRAYBUFFER":
            try {
                r = new ArrayBuffer(0)
            } catch (e) {
                throw Error("ARRAYBUFFER not supported by this environment")
            }
            r = function(e) {
                return h(e, i)
            }
            ;
            break;
        default:
            throw Error("outputFormat must be HEX, B64, BYTES, or ARRAYBUFFER")
        }
        return a = c(g.slice(), _, b, l(o), i),
        v = u(O, Y(e)),
        v = c(a, i, s, v, i),
        r(v)
    }
}
function i(e, t) {
    this.a = e,
    this.b = t
}
function s(e, t, n) {
    var r, o, a, i, s, u = e.length;
    if (t = t || [0],
    n = n || 0,
    s = n >>> 3,
    0 != u % 2)
        throw Error("String of HEX type must be in byte increments");
    for (r = 0; r < u; r += 2) {
        if (o = parseInt(e.substr(r, 2), 16),
        isNaN(o))
            throw Error("String of HEX type contains invalid characters");
        for (i = (r >>> 1) + s,
        a = i >>> 2; t.length <= a; )
            t.push(0);
        t[a] |= o << 8 * (3 - i % 4)
    }
    return {
        value: t,
        binLen: 4 * u + n
    }
}
function u(e, t, n) {
    var r, o, a, i, s = [], s = t || [0];
    for (n = n || 0,
    o = n >>> 3,
    r = 0; r < e.length; r += 1)
        t = e.charCodeAt(r),
        i = r + o,
        a = i >>> 2,
        s.length <= a && s.push(0),
        s[a] |= t << 8 * (3 - i % 4);
    return {
        value: s,
        binLen: 8 * e.length + n
    }
}
function c(e, t, n) {
    var r, o, a, i, s, u, c = [], l = 0, c = t || [0];
    if (n = n || 0,
    t = n >>> 3,
    -1 === e.search(/^[a-zA-Z0-9=+\/]+$/))
        throw Error("Invalid character in base-64 string");
    if (o = e.indexOf("="),
    e = e.replace(/\=/g, ""),
    -1 !== o && o < e.length)
        throw Error("Invalid '=' found in base-64 string");
    for (o = 0; o < e.length; o += 4) {
        for (s = e.substr(o, 4),
        a = i = 0; a < s.length; a += 1)
            r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".indexOf(s[a]),
            i |= r << 18 - 6 * a;
        for (a = 0; a < s.length - 1; a += 1) {
            for (u = l + t,
            r = u >>> 2; c.length <= r; )
                c.push(0);
            c[r] |= (i >>> 16 - 8 * a & 255) << 8 * (3 - u % 4),
            l += 1
        }
    }
    return {
        value: c,
        binLen: 8 * l + n
    }
}
function l(e, t, n) {
    var r, o, a, i = [], i = t || [0];
    for (n = n || 0,
    r = n >>> 3,
    t = 0; t < e.byteLength; t += 1)
        a = t + r,
        o = a >>> 2,
        i.length <= o && i.push(0),
        i[o] |= e[t] << 8 * (3 - a % 4);
    return {
        value: i,
        binLen: 8 * e.byteLength + n
    }
}
function f(e, t, n) {
    var r = "";
    t /= 8;
    var o, a;
    for (o = 0; o < t; o += 1)
        a = e[o >>> 2] >>> 8 * (3 - o % 4),
        r += "0123456789abcdef".charAt(a >>> 4 & 15) + "0123456789abcdef".charAt(15 & a);
    return n.outputUpper ? r.toUpperCase() : r
}
function d(e, t, n) {
    var r, o, a, i = "", s = t / 8;
    for (r = 0; r < s; r += 3)
        for (o = r + 1 < s ? e[r + 1 >>> 2] : 0,
        a = r + 2 < s ? e[r + 2 >>> 2] : 0,
        a = (e[r >>> 2] >>> 8 * (3 - r % 4) & 255) << 16 | (o >>> 8 * (3 - (r + 1) % 4) & 255) << 8 | a >>> 8 * (3 - (r + 2) % 4) & 255,
        o = 0; 4 > o; o += 1)
            i += 8 * r + 6 * o <= t ? "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(a >>> 6 * (3 - o) & 63) : n.b64Pad;
    return i
}
function p(e, t) {
    var n, r, o = "", a = t / 8;
    for (n = 0; n < a; n += 1)
        r = e[n >>> 2] >>> 8 * (3 - n % 4) & 255,
        o += String.fromCharCode(r);
    return o
}
function h(e, t) {
    var n, r = t / 8, o = new ArrayBuffer(r);
    for (n = 0; n < r; n += 1)
        o[n] = e[n >>> 2] >>> 8 * (3 - n % 4) & 255;
    return o
}
function m(e) {
    var t = {
        outputUpper: !1,
        b64Pad: "=",
        shakeLen: -1
    };
    if (e = e || {},
    t.outputUpper = e.outputUpper || !1,
    !0 === e.hasOwnProperty("b64Pad") && (t.b64Pad = e.b64Pad),
    !0 === e.hasOwnProperty("shakeLen")) {
        if (0 != e.shakeLen % 8)
            throw Error("shakeLen must be a multiple of 8");
        t.shakeLen = e.shakeLen
    }
    if ("boolean" != typeof t.outputUpper)
        throw Error("Invalid outputUpper formatting option");
    if ("string" != typeof t.b64Pad)
        throw Error("Invalid b64Pad formatting option");
    return t
}
function y(e, t) {
    var n;
    switch (t) {
    case "UTF8":
    case "UTF16BE":
    case "UTF16LE":
        break;
    default:
        throw Error("encoding must be UTF8, UTF16BE, or UTF16LE")
    }
    switch (e) {
    case "HEX":
        n = s;
        break;
    case "TEXT":
        n = function(e, n, r) {
            var o, a, i, s, u, c = [], l = [], f = 0, c = n || [0];
            if (n = r || 0,
            i = n >>> 3,
            "UTF8" === t)
                for (o = 0; o < e.length; o += 1)
                    for (r = e.charCodeAt(o),
                    l = [],
                    128 > r ? l.push(r) : 2048 > r ? (l.push(192 | r >>> 6),
                    l.push(128 | 63 & r)) : 55296 > r || 57344 <= r ? l.push(224 | r >>> 12, 128 | r >>> 6 & 63, 128 | 63 & r) : (o += 1,
                    r = 65536 + ((1023 & r) << 10 | 1023 & e.charCodeAt(o)),
                    l.push(240 | r >>> 18, 128 | r >>> 12 & 63, 128 | r >>> 6 & 63, 128 | 63 & r)),
                    a = 0; a < l.length; a += 1) {
                        for (u = f + i,
                        s = u >>> 2; c.length <= s; )
                            c.push(0);
                        c[s] |= l[a] << 8 * (3 - u % 4),
                        f += 1
                    }
            else if ("UTF16BE" === t || "UTF16LE" === t)
                for (o = 0; o < e.length; o += 1) {
                    for (r = e.charCodeAt(o),
                    "UTF16LE" === t && (a = 255 & r,
                    r = a << 8 | r >>> 8),
                    u = f + i,
                    s = u >>> 2; c.length <= s; )
                        c.push(0);
                    c[s] |= r << 8 * (2 - u % 4),
                    f += 2
                }
            return {
                value: c,
                binLen: 8 * f + n
            }
        }
        ;
        break;
    case "B64":
        n = c;
        break;
    case "BYTES":
        n = u;
        break;
    case "ARRAYBUFFER":
        try {
            n = new ArrayBuffer(0)
        } catch (e) {
            throw Error("ARRAYBUFFER not supported by this environment")
        }
        n = l;
        break;
    default:
        throw Error("format must be HEX, TEXT, B64, BYTES, or ARRAYBUFFER")
    }
    return n
}
function v(e, t) {
    return e << t | e >>> 32 - t
}
function b(e, t) {
    return 32 < t ? (t -= 32,
    new i(e.b << t | e.a >>> 32 - t,e.a << t | e.b >>> 32 - t)) : 0 !== t ? new i(e.a << t | e.b >>> 32 - t,e.b << t | e.a >>> 32 - t) : e

}
function g(e, t) {
    return e >>> t | e << 32 - t
}
function _(e, t) {
    var n = null
      , n = new i(e.a,e.b);
    return n = 32 >= t ? new i(n.a >>> t | n.b << 32 - t & 4294967295,n.b >>> t | n.a << 32 - t & 4294967295) : new i(n.b >>> t - 32 | n.a << 64 - t & 4294967295,n.a >>> t - 32 | n.b << 64 - t & 4294967295)
}
function w(e, t) {
    return 32 >= t ? new i(e.a >>> t,e.b >>> t | e.a << 32 - t & 4294967295) : new i(0,e.a >>> t - 32)
}
function E(e, t, n) {
    return e & t ^ ~e & n
}
function O(e, t, n) {
    return new i(e.a & t.a ^ ~e.a & n.a,e.b & t.b ^ ~e.b & n.b)
}
function k(e, t, n) {
    return e & t ^ e & n ^ t & n
}
function T(e, t, n) {
    return new i(e.a & t.a ^ e.a & n.a ^ t.a & n.a,e.b & t.b ^ e.b & n.b ^ t.b & n.b)
}
function S(e) {
    return g(e, 2) ^ g(e, 13) ^ g(e, 22)
}
function C(e) {
    var t = _(e, 28)
      , n = _(e, 34);
    return e = _(e, 39),
    new i(t.a ^ n.a ^ e.a,t.b ^ n.b ^ e.b)
}
function M(e) {
    return g(e, 6) ^ g(e, 11) ^ g(e, 25)
}
function P(e) {
    var t = _(e, 14)
      , n = _(e, 18);
    return e = _(e, 41),
    new i(t.a ^ n.a ^ e.a,t.b ^ n.b ^ e.b)
}
function j(e) {
    return g(e, 7) ^ g(e, 18) ^ e >>> 3
}
function D(e) {
    var t = _(e, 1)
      , n = _(e, 8);
    return e = w(e, 7),
    new i(t.a ^ n.a ^ e.a,t.b ^ n.b ^ e.b)
}
function A(e) {
    return g(e, 17) ^ g(e, 19) ^ e >>> 10
}
function x(e) {
    var t = _(e, 19)
      , n = _(e, 61);
    return e = w(e, 6),
    new i(t.a ^ n.a ^ e.a,t.b ^ n.b ^ e.b)
}
function L(e, t) {
    var n = (65535 & e) + (65535 & t);
    return ((e >>> 16) + (t >>> 16) + (n >>> 16) & 65535) << 16 | 65535 & n
}
function I(e, t, n, r) {
    var o = (65535 & e) + (65535 & t) + (65535 & n) + (65535 & r);
    return ((e >>> 16) + (t >>> 16) + (n >>> 16) + (r >>> 16) + (o >>> 16) & 65535) << 16 | 65535 & o
}
function N(e, t, n, r, o) {
    var a = (65535 & e) + (65535 & t) + (65535 & n) + (65535 & r) + (65535 & o);
    return ((e >>> 16) + (t >>> 16) + (n >>> 16) + (r >>> 16) + (o >>> 16) + (a >>> 16) & 65535) << 16 | 65535 & a
}
function R(e, t) {
    var n, r, o;
    return n = (65535 & e.b) + (65535 & t.b),
    r = (e.b >>> 16) + (t.b >>> 16) + (n >>> 16),
    o = (65535 & r) << 16 | 65535 & n,
    n = (65535 & e.a) + (65535 & t.a) + (r >>> 16),
    r = (e.a >>> 16) + (t.a >>> 16) + (n >>> 16),
    new i((65535 & r) << 16 | 65535 & n,o)
}
function F(e, t, n, r) {
    var o, a, s;
    return o = (65535 & e.b) + (65535 & t.b) + (65535 & n.b) + (65535 & r.b),
    a = (e.b >>> 16) + (t.b >>> 16) + (n.b >>> 16) + (r.b >>> 16) + (o >>> 16),
    s = (65535 & a) << 16 | 65535 & o,
    o = (65535 & e.a) + (65535 & t.a) + (65535 & n.a) + (65535 & r.a) + (a >>> 16),
    a = (e.a >>> 16) + (t.a >>> 16) + (n.a >>> 16) + (r.a >>> 16) + (o >>> 16),
    new i((65535 & a) << 16 | 65535 & o,s)
}
function H(e, t, n, r, o) {
    var a, s, u;
    return a = (65535 & e.b) + (65535 & t.b) + (65535 & n.b) + (65535 & r.b) + (65535 & o.b),
    s = (e.b >>> 16) + (t.b >>> 16) + (n.b >>> 16) + (r.b >>> 16) + (o.b >>> 16) + (a >>> 16),
    u = (65535 & s) << 16 | 65535 & a,
    a = (65535 & e.a) + (65535 & t.a) + (65535 & n.a) + (65535 & r.a) + (65535 & o.a) + (s >>> 16),
    s = (e.a >>> 16) + (t.a >>> 16) + (n.a >>> 16) + (r.a >>> 16) + (o.a >>> 16) + (a >>> 16),
    new i((65535 & s) << 16 | 65535 & a,u)
}
function z(e) {
    var t, n = 0, r = 0;
    for (t = 0; t < arguments.length; t += 1)
        n ^= arguments[t].b,
        r ^= arguments[t].a;
    return new i(r,n)
}
function Y(e) {
    var t, n = [];
    if ("SHA-1" === e)
        n = [1732584193, 4023233417, 2562383102, 271733878, 3285377520];
    else if (0 === e.lastIndexOf("SHA-", 0))
        switch (n = [3238371032, 914150663, 812702999, 4144912697, 4290775857, 1750603025, 1694076839, 3204075428],
        t = [1779033703, 3144134277, 1013904242, 2773480762, 1359893119, 2600822924, 528734635, 1541459225],
        e) {
        case "SHA-224":
            break;
        case "SHA-256":
            n = t;
            break;
        case "SHA-384":
            n = [new i(3418070365,n[0]), new i(1654270250,n[1]), new i(2438529370,n[2]), new i(355462360,n[3]), new i(1731405415,n[4]), new i(41048885895,n[5]), new i(3675008525,n[6]), new i(1203062813,n[7])];
            break;
        case "SHA-512":
            n = [new i(t[0],4089235720), new i(t[1],2227873595), new i(t[2],4271175723), new i(t[3],1595750129), new i(t[4],2917565137), new i(t[5],725511199), new i(t[6],4215389547), new i(t[7],327033209)];
            break;
        default:
            throw Error("Unknown SHA variant")
        }
    else {
        if (0 !== e.lastIndexOf("SHA3-", 0) && 0 !== e.lastIndexOf("SHAKE", 0))
            throw Error("No SHA variants supported");
        for (e = 0; 5 > e; e += 1)
            n[e] = [new i(0,0), new i(0,0), new i(0,0), new i(0,0), new i(0,0)]
    }
    return n
}
function B(e, t) {
    var n, r, o, a, i, s, u, c = [];
    for (n = t[0],
    r = t[1],
    o = t[2],
    a = t[3],
    i = t[4],
    u = 0; 80 > u; u += 1)
        c[u] = 16 > u ? e[u] : v(c[u - 3] ^ c[u - 8] ^ c[u - 14] ^ c[u - 16], 1),
        s = 20 > u ? N(v(n, 5), r & o ^ ~r & a, i, 1518500249, c[u]) : 40 > u ? N(v(n, 5), r ^ o ^ a, i, 1859775393, c[u]) : 60 > u ? N(v(n, 5), k(r, o, a), i, 2400959708, c[u]) : N(v(n, 5), r ^ o ^ a, i, 3395469782, c[u]),
        i = a,
        a = o,
        o = v(r, 30),
        r = n,
        n = s;
    return t[0] = L(n, t[0]),
    t[1] = L(r, t[1]),
    t[2] = L(o, t[2]),
    t[3] = L(a, t[3]),
    t[4] = L(i, t[4]),
    t
}
function U(e, t, n, r) {
    var o;
    for (o = 15 + (t + 65 >>> 9 << 4); e.length <= o; )
        e.push(0);
    for (e[t >>> 5] |= 128 << 24 - t % 32,
    t += n,
    e[o] = 4294967295 & t,
    e[o - 1] = t / 4294967296 | 0,
    t = e.length,
    o = 0; o < t; o += 16)
        r = B(e.slice(o, o + 16), r);
    return r
}
function q(e, t, n) {
    var r, o, a, s, u, c, l, f, d, p, h, m, y, v, b, g, _, w, z, Y, B, U, q, V = [];
    if ("SHA-224" === n || "SHA-256" === n)
        p = 64,
        m = 1,
        U = Number,
        y = L,
        v = I,
        b = N,
        g = j,
        _ = A,
        w = S,
        z = M,
        B = k,
        Y = E,
        q = W;
    else {
        if ("SHA-384" !== n && "SHA-512" !== n)
            throw Error("Unexpected error in SHA-2 implementation");
        p = 80,
        m = 2,
        U = i,
        y = R,
        v = F,
        b = H,
        g = D,
        _ = x,
        w = C,
        z = P,
        B = T,
        Y = O,
        q = G
    }
    for (n = t[0],
    r = t[1],
    o = t[2],
    a = t[3],
    s = t[4],
    u = t[5],
    c = t[6],
    l = t[7],
    h = 0; h < p; h += 1)
        16 > h ? (d = h * m,
        f = e.length <= d ? 0 : e[d],
        d = e.length <= d + 1 ? 0 : e[d + 1],
        V[h] = new U(f,d)) : V[h] = v(_(V[h - 2]), V[h - 7], g(V[h - 15]), V[h - 16]),
        f = b(l, z(s), Y(s, u, c), q[h], V[h]),
        d = y(w(n), B(n, r, o)),
        l = c,
        c = u,
        u = s,
        s = y(a, f),
        a = o,
        o = r,
        r = n,
        n = y(f, d);
    return t[0] = y(n, t[0]),
    t[1] = y(r, t[1]),
    t[2] = y(o, t[2]),
    t[3] = y(a, t[3]),
    t[4] = y(s, t[4]),
    t[5] = y(u, t[5]),
    t[6] = y(c, t[6]),
    t[7] = y(l, t[7]),
    t
}
function V(e, t) {
    var n, r, o, a, s = [], u = [];
    if (null !== e)
        for (r = 0; r < e.length; r += 2)
            t[(r >>> 1) % 5][(r >>> 1) / 5 | 0] = z(t[(r >>> 1) % 5][(r >>> 1) / 5 | 0], new i((255 & e[r + 1]) << 24 | (65280 & e[r + 1]) << 8 | (16711680 & e[r + 1]) >>> 8 | e[r + 1] >>> 24,(255 & e[r]) << 24 | (65280 & e[r]) << 8 | (16711680 & e[r]) >>> 8 | e[r] >>> 24));
    for (n = 0; 24 > n; n += 1) {
        for (a = Y("SHA3-"),
        r = 0; 5 > r; r += 1)
            s[r] = z(t[r][0], t[r][1], t[r][2], t[r][3], t[r][4]);
        for (r = 0; 5 > r; r += 1)
            u[r] = z(s[(r + 4) % 5], b(s[(r + 1) % 5], 1));
        for (r = 0; 5 > r; r += 1)
            for (o = 0; 5 > o; o += 1)
                t[r][o] = z(t[r][o], u[r]);
        for (r = 0; 5 > r; r += 1)
            for (o = 0; 5 > o; o += 1)
                a[o][(2 * r + 3 * o) % 5] = b(t[r][o], K[r][o]);
        for (r = 0; 5 > r; r += 1)
            for (o = 0; 5 > o; o += 1)
                t[r][o] = z(a[r][o], new i(~a[(r + 1) % 5][o].a & a[(r + 2) % 5][o].a,~a[(r + 1) % 5][o].b & a[(r + 2) % 5][o].b));
        t[0][0] = z(t[0][0], Q[n])
    }
    return t
}


function run(e,n){
    client_id = 'c3cef7c66a1843f8b3a9e6a1e3160e20';
    r = new a("SHA-1", "TEXT");
    r.setHMACKey("d1b964811afb40118a12068ff74a12f4", "TEXT");
    r.update(e);
    r.update(client_id);
    r.update("com.zhihu.web");
    r.update(String(n));
    return r.getHMAC("HEX")
}