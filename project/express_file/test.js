Vd = function e(a) {
    function t(e, a) {
        return e >>> a | e << 32 - a
    }
    for (var n, r, i = Math.pow, o = i(2, 32), c = "", s = [], l = 8 * a.length, u = e.h = e.h || [], d = e.k = e.k || [], p = d.length, m = {}, f = 2; p < 64; f++)
        if (!m[f]) {
            for (n = 0; n < 313; n += f)
                m[n] = f;
            u[p] = i(f, .5) * o | 0,
            d[p++] = i(f, 1 / 3) * o | 0
        }
    for (a += "\x80"; a.length % 64 - 56; )
        a += "\0";
    for (n = 0; n < a.length; n++) {
        if ((r = a.charCodeAt(n)) >> 8)
            return;
        s[n >> 2] |= r << (3 - n) % 4 * 8
    }
    for (s[s.length] = l / o | 0,
    s[s.length] = l,
    r = 0; r < s.length; ) {
        var h = s.slice(r, r += 16)
          , g = u;
        for (u = u.slice(0, 8),
        n = 0; n < 64; n++) {
            var y = h[n - 15]
              , E = h[n - 2]
              , b = u[0]
              , v = u[4]
              , O = u[7] + (t(v, 6) ^ t(v, 11) ^ t(v, 25)) + (v & u[5] ^ ~v & u[6]) + d[n] + (h[n] = n < 16 ? h[n] : h[n - 16] + (t(y, 7) ^ t(y, 18) ^ y >>> 3) + h[n - 7] + (t(E, 17) ^ t(E, 19) ^ E >>> 10) | 0);
            (u = [O + ((t(b, 2) ^ t(b, 13) ^ t(b, 22)) + (b & u[1] ^ b & u[2] ^ u[1] & u[2])) | 0].concat(u))[4] = u[4] + O | 0
        }
        for (n = 0; n < 8; n++)
            u[n] = u[n] + g[n] | 0
    }
    for (n = 0; n < 8; n++)
        for (r = 3; r + 1; r--) {
            var k = u[n] >> 8 * r & 255;
            c += (k < 16 ? 0 : "") + k.toString(16)
        }
    return c
}

let d = "cf30f99055318c86e049fa3c9c886d5b_K_»¹²>DõWJ6äÞ";
result = Vd(d)
console.log(result)