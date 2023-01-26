$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(characters) {
  $('DIV#character').text(characters.name); }, "json");
