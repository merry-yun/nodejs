const express = require('express');

const hostname = 'localhost';
const port = 8083;

const app = express();
app.use('views', '/path/to/templates');
app.use('view engine', 'hbs');

app.get('/', (req, res) => {
  res.render('index');
});


app.listen(port, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});