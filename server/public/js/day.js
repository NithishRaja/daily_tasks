let dayApp = Vue.createApp({})

let dayCardTweetsListItem = ('song-card-tweets-list-item', {
  template: "<div class='accordion-item'><h2 class='accordion-header' :id='\"tweetAccordionHeading\" + index'>"+
  "<button class='accordion-button collapsed' type='button' data-bs-toggle='collapse' :data-bs-target='\"#tweetsAccordionBody\" + index' aria-expanded='false' :aria-controls='\"tweetsAccordionBody\" + index'>"+
  "<img class='me-1' style='border-radius: 50%;' :src='tweet.profile_image_url' />{{tweet.name}}<br>@{{tweet.username}}</button></h2>"+
  "<div :id='\"tweetsAccordionBody\" + index' class='accordion-collapse collapse' :aria-labelledby='\"tweetsAccordionBody\" + index' data-bs-parent='tweetsAccordion'>"+
  "<div class='accordion-body'><span v-for='line in tweet.text'><strong v-if='line.type != \"text\"'>{{line.text}}</strong><template v-else>{{line.text}}</template></span>"+
  "<div class='card-body text-end'><a class='btn btn-primary' target='_blank' :href='tweet.tweet_url'>View tweet</a></div></div></div></div>",
  props: ["index", "tweet"]
})

let dayCardTweetsList = ('song-card-tweets-list', {
  template: "<div v-if='tweets.length == 0' class='card-footer'>No tweets to show</div>"+
  "<div v-if='tweets.length != 0' class='accordion accordion-flush' id='tweetsAccordion'>"+
  "<day-card-tweets-list-item v-for='(tweet, index) in tweets' :index='index' :tweet='tweet'/></div>",
  props: ["tweets"],
  components: {
    "day-card-tweets-list-item": dayCardTweetsListItem
  }
})

dayApp.component("day-card", {
  template: "<div class='card'>"+
  "<div class='card-body text-center'><h5 class='card-title'>{{day.text}}</h5></div>"+
  "<div class='card-body text-end'><a class='btn btn-primary' target='_blank' :href='day.link'>Read more...</a></div>"+
  "<day-card-tweets-list v-if='day.tweet' :tweets='day.tweet'/>"+
  "</div>",
  components: {
    "day-card-tweets-list": dayCardTweetsList
  },
  data(){
    return {
      day: {}
    }
  },
  created(){
    // Read in day
    fetch('/data?key=day')
    .then(response => response.json())
    .then(data => {
      for(let i=0;i<data.tweet.length;++i){
        data.tweet[i].tweet_url = 'https://twitter.com/'+data.tweet[i].username+'/status/'+data.tweet[i].id
      }
      this.day = data;
    });
  }
})

dayApp.mount("#day-section")
