preload_end();


function fetch_hello(){
    preload_start();
    fetch('/api')
    .then(response => response.json())
    .then(data => {
        preload_end();
        console.log(data);
     });
}


var app = new Vue({

  //element selector (by id in this case) where the app is mounted
  el: '#app',

  //customize delimiters to avoid conflict with jinja
  delimiters: ['[[', ']]'],

  //data elements
  data: {
    message: 'Hello Vue!'
  },

  components: {
    'test-component': httpVueLoader('template.vue')
  },

  //registered methods and functions
  methods: {

  }

});


Vue.component('todo-item', {
  // The todo-item component now accepts a
  // "prop", which is like a custom attribute.
  // This prop is called todo.
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
})