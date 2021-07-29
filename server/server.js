/**
  * File containing server code
  *
  */

// importing vendor modules
const express = require('express');
const path = require('path');
var bodyparser = require("body-parser");

// importing local modules

// initializing express app
const app = express();

// setting port value
app.set("port", process.env.PORT || 8000);

// using body-parser to read post info
app.use(bodyparser.urlencoded({extended:true}));
app.use(bodyparser.json());

// Serve static files from the React app
app.use(express.static(path.join(__dirname, 'public')));

let data;

process.stdin.on('data', payload => {
  data = JSON.parse(payload);
});

app.get('/data', function (req, res) {
  // Check if key exists in query parameters
  if("key" in res.req.query){
    // Extract key
    key = res.req.query.key;
    // Check if key exists in data
    if(key in data){
      res.status(200).end(JSON.stringify(data[key]));
    }else{
      res.status(404).end();
    }
  }else{
    res.status(400).end()
  }
});

app.get('/', function (req, res) {
  res.send(`got to /data`);
});

// listening to port
app.listen(app.get("port"), function(err){
  if(err) return console.log(err);
  console.log("Server is running on port %d, press Ctrl+C to close", app.get("port"));
});
