var CryptoJS = require("crypto-js")

const key = 'qyrohlf5sjazleru'
const iv = '1980233449'

// 加密
function Encrypt (text) {
  return CryptoJS.AES.encrypt(text, CryptoJS.enc.Utf8.parse(key), {
    iv: CryptoJS.enc.Utf8.parse(iv),
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
  }).toString()
}

// 解密
function Decrypt (text) {
  let decrypted = CryptoJS.AES.decrypt(text, CryptoJS.enc.Utf8.parse(key), {
    iv: CryptoJS.enc.Utf8.parse(iv),
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs7
  })
  return decrypted.toString(CryptoJS.enc.Utf8)
}

var word = "ea6f62dad8ee40638832f3bd125f1a37"
var result = Encrypt(word)
console.log(result)

