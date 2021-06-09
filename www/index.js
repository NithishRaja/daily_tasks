var app = Vue.createApp({
  data(){
    return {
      song: {},
      quote: {},
      day: {},
      score: {}
    }
  },
  computed: {

  },
  methods: {

  },
  mounted(){
    // Read in quote data
    fetch('http://localhost:8000/data/quote.json')
    .then(response => response.json())
    .then(data => this.quote = data);
    // Read in song data
    fetch('http://localhost:8000/data/song.json')
    .then(response => response.json())
    .then(data => this.song = data);
    // Read in day data
    fetch('http://localhost:8000/data/day.json')
    .then(response => response.json())
    .then(data => this.day = data);
    // Read in score data
    fetch('http://localhost:8000/data/score.json')
    .then(response => response.json())
    .then(data => this.score = data);
  },
  updated(){

  }
}).mount("body")
