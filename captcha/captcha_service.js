let express = require('express');
let app = express();
let bodyParser = require('body-parser');
const child_process = require('child_process');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));


app.post('/api/v1/captche', function(req, res){
    let content = req.body;
    const {img_byte, type} = content;
    console.log(img_byte)
    if (type == 1){
        img_str = ImgToStr(img_byte)
        data = {
            img_code: img_str,
            code: 200,
            message: "succeed"
        }
    }else{
        data ={
            code:200,
            message: "fail",
            img: ""
        }
    }
    response = {
        data: data
    };
    res.end(JSON.stringify(response));
})

var server = app.listen(8081, function () {

  let host = server.address().address
  let port = server.address().port

  console.log("应用实例，访问地址为 http://%s:%s", host, port)

})

function ImgToStr(img){
    py_file = "captcha_verfiry.py "
    cmd = 'python ' + py_file + img
    img_str = child_process.execSync(cmd, function (error, stdout, stderr) { 
        if (error) {
            console.log(error.stack);            
            console.log('Error code: '+ error.code);            
            console.log('Signal received: '+ error.signal);
            }        
    }).toString();
    console.log(img_str)
    result = img_str.split('\r\n')[1]
    return result
}