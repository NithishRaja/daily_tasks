let wordsApp = Vue.createApp({})

let wordsCardItem = ("words-card-item", {
  template: "<div class='accordion-item'><h2 class='accordion-header' :id='\"wordsAccordionHeading\" + index'>"+
  "<button class='accordion-button collapsed' type='button' data-bs-toggle='collapse' :data-bs-target='\"#wordsAccordionBody\" + index' aria-expanded='false' :aria-controls='\"wordsAccordionBody\" + index'>"+
  "{{word.word}}<br>{{word.wordType}} . {{word.pronunciation}}</button></h2>"+
  "<div :id='\"wordsAccordionBody\" + index' class='accordion-collapse collapse' :aria-labelledby='\"wordsAccordionBody\" + index' data-bs-parent='wordsAccordion'>"+
  "<ul class='list-group list-group-flush'><li v-for='text in word.meaning' class='list-group-item'>{{text}}</li></ul></div></div>",
  props: ["word", "index"]
})

wordsApp.component("words-card", {
  template: "<div class='card'><div class='card-header'>Words of the day</div><div v-if='words.length == 0' class='card-body'>No words to show</div>"+
  "<div v-if='words.length != 0' class='accordion accordion-flush' id='wordsAccordion'>"+
  "<words-card-item v-for='(item, index) in words' :word='item' :index='index' /></div></div>",
  components: {
    "words-card-item": wordsCardItem
  },
  data(){
    return {
      words: []
    }
  },
  created(){
    // Read in day
    fetch('/data?key=word')
    .then(response => response.json())
    .then(data => this.words = data);
  }
})

wordsApp.mount("#words-section")
