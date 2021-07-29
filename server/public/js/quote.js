let quoteApp = Vue.createApp({})

quoteApp.component("quote-card", {
  template: "<div class='card'>"+
  "<div class='card-header text-center'>{{quote.topic}}</div>"+
  "<div class='card-body'><blockquote class='blockquote'><p>{{quote.text}}</p></blockquote>"+
  "<div class='blockquote-footer text-end'><cite>{{quote.author}}</cite></div></div>"+
  "</div>",
  components: {},
  data(){
    return {
      quote: {}
    }
  },
  created(){
    // Read in quote
    fetch('/data?key=quote')
    .then(response => response.json())
    .then(data => this.quote = data);
  }
})

quoteApp.mount("#quote-section")
