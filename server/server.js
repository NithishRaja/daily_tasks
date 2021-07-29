/****
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

// Initialise variable to hold data
let data;

// /*
data = {
  "quote": {'topic': 'Topics', 'text': 'To refactor or to start from scratch?', 'author': 'Cocoa Puffs'},
  "word": [{'word': 'celerity', 'wordType': 'noun', 'pronunciation': 'suh-ler-i-tee', 'meaning': [': rapidity of motion or action']}, {'word': 'palaver', 'wordType': 'noun', 'pronunciation': 'puh-LAV-er', 'meaning': [': a long parley usually between persons of different cultures or levels of sophistication', ': conference, discussion']}],
  "song": {'title': 'Things A Man Oughta Know', 'artist': {'artist': ['Lainey Wilson'], 'featured': []}, 'info': ['59 Last Week', '51 Peak Rank', '10 Weeks on Chart'], 'lyrics': [['I can hook a trailer on a two-inch hitch', 'I can shoot a shotgun, I can catch a fish', 'I can change a tire on the side of a road', 'Yeah, I know a few things a man oughta know'], ["How to know when it's love", "How to stay when it's tough", "How to know you're messin' up a good thing", "And how to fix it 'fore it's too late", 'And yeah, I know a boy', 'Who gave up and got it wrong', "If you really love a woman, you don't let her go", 'Yeah, I know a few things a man oughta know'], ["If I can't have it, I can do without", 'I can hang a picture same as I can take it down', 'And how to keep it hidden when a heart gets broke', 'Yeah, I know a few things a man oughta know'], ["How to know when it's love", "How to stay when it's tough", "How to know you're messin' up a good thing", "And how to fix it 'fore it's too late", 'And yeah, I know a boy', 'Who gave up and got it wrong', "If you really love a woman, you don't let her go", 'Yeah, I know a few things a man oughta know'], ['I...'], ["How to know when it's love", "How to stay when it's tough", 'How to chase forever down a driveway', 'How to never let it get there in the first place', 'And yeah, I know a boy', 'Who gave up and got it wrong', "If you really love a woman, you don't let her go", 'Well, I know a few things a man oughta know', 'Yeah, I know a few things a man oughta know']], 'video': {'watch': 'https://www.youtube.com/watch?v=dqINSvm3Psw', 'lyric': 'https://www.youtube.com/watch?v=umjLFOc6hLo'}},
  "day": {'text': 'International Tiger Day', 'link': 'https://www.daysoftheyear.com/days/international-tiger-day/', 'tweet': [{'name': 'Ivy Enterprises', 'username': 'EnterprisesIvy', 'profile_image_url': 'https://pbs.twimg.com/profile_images/1223616102619500545/9VdnOO-n_normal.jpg', 'id': '1420694110395060224', 'text': [{'text': 'International Tiger Day 2021: Sachin Tendulkar, Anil Kumble Spread\xa0Awareness', 'type': 'text'}]}, {'name': 'SOUMIT DAS', 'username': 'soumitd', 'profile_image_url': 'https://pbs.twimg.com/profile_images/1152576111185780737/4sndjOv0_normal.png', 'id': '1420694067365564421', 'text': [{'text': '#InternationalTigerDay\n\n#Tiger', 'type': 'special'}, {'text': ' is a symbol of ', 'type': 'text'}, {'text': '#Beauty', 'type': 'special'}, {'text': ' , ', 'type': 'text'}, {'text': '#Bravery', 'type': 'special'}, {'text': ' , ', 'type': 'text'}, {'text': '#Strength', 'type': 'special'}, {'text': ' and ', 'type': 'text'}, {'text': '#Nationality.', 'type': 'special'}, {'text': ' So ', 'type': 'text'}, {'text': '#Save', 'type': 'special'}, {'text': ' the Tiger and Save the ', 'type': 'text'}, {'text': "#Nation's", 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#Pride.', 'type': 'special'}, {'text': ' Happy International Tiger Day !\n\n- Team Financial Goal Achievers', 'type': 'text'}]}, {'name': 'Indrabhuwan Kumar Singh', 'username': 'ibksingh', 'profile_image_url': 'https://pbs.twimg.com/profile_images/1249381443576500224/9Licjjl__normal.jpg', 'id': '1420694048034066434', 'text': [{'text': 'On the international tiger day - we should take oath to save them\n\nSave the tigers before they are silenced forever. Killing tigers is the greed, not the need. Save Tiger! Save Nature!\n.\n', 'type': 'text'}, {'text': '#tikbitz', 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#tikbitz2021', 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#tiger', 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#wildlife', 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#animals', 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#nature', 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#tigers', 'type': 'special'}, {'text': '  ', 'type': 'text'}, {'text': '#animal', 'type': 'special'}, {'text': ' ', 'type': 'text'}, {'text': '#wildlifephotography', 'type': 'hashtag'}]}]},
  "event": [{'name': 'hehehehe2', 'date': {'day': 10, 'month': 10, 'year': 2021}}, {'name': 'hehehehe2', 'date': {'day': 13, 'month': 10, 'year': 2021}}, {'name': 'hehehehe1', 'date': {'day': 10, 'month': 10, 'year': 2021}}],
  "score": [{'gameId': '0042000406', 'boxscoreURL': 'https://global.nba.com/boxscore/#!/0042000406', 'title': ' ROUND 4', 'subtitle': 'MIL wins 4-2', 'clock': "FINAL", 'hTeam': {'id': '1610612749', 'triCode': 'MIL', 'score': ['29', '13', '35', '28', '105']}, 'vTeam': {'id': '1610612756', 'triCode': 'PHX', 'score': ['16', '31', '30', '21', '105']}}]
};
// */

// Add listener for getting data
process.stdin.on('data', payload => {
  data = JSON.parse(payload);
});

// Add route handler for '/data' route
app.get('/data', function (req, res) {
  // Check if key exists in query parameters
  if("key" in res.req.query){
    // Extract key
    key = res.req.query.key;
    // Check if key exists in data
    if(key in data){
      // Return data
      res.status(200).end(JSON.stringify(data[key]));
    }else{
      // Key does not exists, return not found
      res.status(404).end();
    }
  }else{
    // No key specified, return bad request
    res.status(400).end()
  }
});

// Add route handler for '/' route
app.get('/', function (req, res) {
  // Return index.html file
  res.sendFile(__dirname+"/public/html/index.html");
});

// listening to port
app.listen(app.get("port"), function(err){
  if(err) return console.log(err);
  console.log("Server is running on port %d, press Ctrl+C to close", app.get("port"));
});
