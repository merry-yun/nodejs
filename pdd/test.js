
let express = require('express');
let app = express();

app.listen(300, function(){
  console.log('start');
})

function middleware1(req, res, next){
  console.log("1111");
}

function middleware2(req, res,next){
  console.log("222");
  middleware3();
  next();
}

function middleware3(req, res, next){
  console.log("3333");
}

app.use(middleware2);