let eventsApp = Vue.createApp({})

eventsApp.component("events-card", {
  template: "<div class='card'>"+
  "<div class='card-header text-center'>Upcoming events</div>"+
  "<div v-if='events.length == 0' class='card-body text-center'>No upcoming events</div>"+
  "<ul class='list-group list-group-flush'><li class='list-group-item' v-for='event in events'>"+
  "<div class='fw-bold'>{{event.name}}</div><span>{{event.date}}</span>"+
  "</li></ul>"+
  "</div>",
  components: {},
  data(){
    return {
      events: []
    }
  },
  created(){
    // Read in events
    fetch('../data/events.json')
    .then(response => response.json())
    .then(data => this.events = data);
  }
})

eventsApp.mount("#events-section")
