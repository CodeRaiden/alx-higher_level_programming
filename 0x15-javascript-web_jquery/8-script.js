$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (titles) {
  $.each(titles['results'], function(data, movies) {
    $("UL#list_movies").append('<li>' + movies['title'] + '</li>');
  }); }, 'json');
