let scoreApp = Vue.createApp({})

let scoreCardGameScoreline = ("score-card-game-scoreline", {
  template: "<tr><th scope='row'>{{team.triCode}}</th>"+
  "<td v-for='item in team.score'>{{item}}</td>"+
  "</tr>",
  props: ["team"]
})

let scoreCardGame = ("score-card-game", {
  template: "<div class='card-body'><h5 class='card-title'>{{game.title}}</h5><h6 class='card-subtitle text-muted'>{{game.subtitle}}</h6>"+
  "<table class='table'><tbody>"+
  "<score-card-game-scoreline :team='game.hTeam' />"+
  "<score-card-game-scoreline :team='game.vTeam' /></tbody></table>"+
  "<div class='row text-center'><div class='col'>{{game.clock}}</div><div class='col'><a target='_blank' :href='game.boxscoreURL' class='btn btn-primary'>View boxscore</a></div></div></div>",
  components: {
    "score-card-game-scoreline": scoreCardGameScoreline
  },
  props: ["game"]
})

scoreApp.component("score-card", {
  template: "<div class='card'><div class='card-header text-center'>NBA scores</div>"+
  "<score-card-game v-for='game in score' :game='game' />"+
  "<div class='card-body text-end'><a class='btn btn-primary' target='_blank' href='https://www.nba.com/standings'>View standings</a></div></div>",
  components: {
    "score-card-game": scoreCardGame
  },
  data(){
    return {
      score: {}
    }
  },
  created(){
    // Read in score
    fetch('/data?key=score')
    .then(response => response.json())
    .then(data => this.score = data);
  }
})

scoreApp.mount("#score-section")
