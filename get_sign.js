
var http = require('http')
var url = require('url')
var sign = require("./sign_v2.js")

router = {
    "toutiaoSign": function(req, res){
        let str='';
        req.on('data', data=>{
            str+=data;
        });
        req.on('end', ()=> {
              let post = str;
              console.log( JSON.parse(post))
              data = JSON.parse(post)
              let signature = sign.toutiao_sign(data['url'], data["cookie"])
              res.writeHead(200, { 'Content-Type': 'application/json' });
              res.end(signature);
        })
  },
    "home": function(){
        console.log("home")
    }
}





http.createServer(function(req, res) {
    // res.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'})
    // res.writeHead(200, {'Content-Type': 'images/jpeg'})
    if (req.url !== '/favicon.ico') {
        var pathName = url.parse(req.url).pathname.replace(/\//, '')
        console.log(pathName);
        try {
            router[pathName](req, res)
        } catch (err) {
            console.log(err)
            router['home'](req, res)
        }

    }
    // res.end();
}).listen(8082);
console.log('Server running at http://localhost:8082')