let songApp = Vue.createApp({})

let songCardTitle = ("song-card-title", {
  template: "<h5 class='card-title'>{{title}}</h5><h6 class='card-subtitle text-muted'>"+
  "<template v-for='item in artist.artist'>{{item}} </template>"+
  "<template v-if='artist.featured.length > 0'> ft. "+
  "<template v-for='item in artist.featured'>{{item}} </template></template></h6>",
  props: ["title", "artist"]
})

let songCardButton = ("song-card-button", {
  template: "<a class='btn btn-primary me-2' target='_blank' :href='link'>{{text}}</a>",
  props: ["text", "link"]
})

let songCardInfoList = ("song-card-info-list", {
  template: "<div class='list-group list-group-flush'>"+
  "<div class='list-group-item' v-for='item in info'>{{item}}</div>"+
  "</div>",
  props: ["info"]
})

let songCardLyrics = ("song-card-lyrics", {
  template: "<div v-if='lyrics.length == 0' class='card-footer'>Could not find lyrics</div>"+
  "<div v-if='lyrics.length != 0' class='accordion accordion-flush' id='lyricsAccordion'>"+
  "<div class='accordion-item'><h2 class='accordion-header' id='lyricsAccordionHeading'>"+
  "<button class='accordion-button collapsed' type='button' data-bs-toggle='collapse' data-bs-target='#lyricsAccordionBody' aria-expanded='false' aria-controls='lyricsAccordionBody'>Lyrics</button></h2>"+
  "<div id='lyricsAccordionBody' class='accordion-collapse collapse' aria-labelledby='lyricsAccordionBody' data-bs-parent='lyricsAccordion'>"+
  "<div class='accordion-body'><p v-for='segment in lyrics'><span v-for='line in segment'>{{line}}<br></span></p>"+
  "</div></div></div></div>",
  props: ["lyrics"]
})

songApp.component("song-card", {
  template: "<div class='card'>"+
  "<div class='card-body'><song-card-title :title='song.title' :artist='song.artist' v-if='song.title' /></div>"+
  "<song-card-info-list v-if='song.info' :info='song.info' />"+
  "<div class='card-body'><song-card-button v-if='song.video' text='watch video' :link='song.video.watch'/>"+
  "<song-card-button v-if='song.video' text='lyrics video' :link='song.video.lyric'/></div>"+
  "<song-card-lyrics v-if='song.lyrics' :lyrics='song.lyrics'/>"+
  "</div>",
  components: {
    "song-card-title": songCardTitle,
    "song-card-button": songCardButton,
    "song-card-info-list": songCardInfoList,
    "song-card-lyrics": songCardLyrics
  },
  data(){
    return {
      song: {}
    }
  },
  created(){
    // Read in song
    fetch('/data?key=song')
    .then(response => response.json())
    .then(data => this.song = data);
  }
})

songApp.mount("#song-section")
