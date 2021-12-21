function stringfiy(words, sigBytes) {
    var t = words
      , n = sigBytes
      , r = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    for (var o = [], i = 0; i < n; i += 3)
        for (var a = (t[i >>> 2] >>> 24 - i % 4 * 8 & 255) << 16 | (t[i + 1 >>> 2] >>> 24 - (i + 1) % 4 * 8 & 255) << 8 | t[i + 2 >>> 2] >>> 24 - (i + 2) % 4 * 8 & 255, l = 0; l < 4 && i + .75 * l < n; l++)
            o.push(r.charAt(a >>> 6 * (3 - l) & 63));
    var s = r.charAt(64);
    if (s)
        for (; o.length % 4; )
            o.push(s);
    return o.join("")
}

  let a = [1999779907, 2050373940, 1932931947, 1113156404]
  let result = stringfiy(a, 16)
  console.log(result)