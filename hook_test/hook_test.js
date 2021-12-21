
function add(a,b){
    return a + b
}
add.prototype.test = function(){
    return "test"
}
add.prototype.toString = function(){
    console.log('enter');
    return "why"
}
console.log(add.prototype)
console.log(add.toString())