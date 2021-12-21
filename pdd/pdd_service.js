var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var crawl = require('./yhpdd.js')
// 创建 application/x-www-form-urlencoded 编码解析
//var urlencodedParser = bodyParser.urlencoded({ extended: false })
// create application/json parser
//var jsonParser = bodyParser.json()
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.get('/pdd_get', function (req, res) {
   // 输出 JSON 格式
   response = {
       crawlinfo: crawl.crawl_info()
   };
   res.end(JSON.stringify(response));
})

app.post('/pdd_post', function (req, res) {
    console.log(req.body);
   // 输出 JSON 格式
   response = {
       crawlinfo: crawl.crawl_info()
   };
//   console.log(response);
   res.end(JSON.stringify(response));
})

var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("应用实例，访问地址为 http://%s:%s", host, port)

})