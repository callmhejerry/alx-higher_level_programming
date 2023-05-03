$("document").ready(() => {
  const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
  $.get(url, (data, status, xhr) => {
    if (status == "success") {
      const { results } = data;
      const li = $("ul#list_movies");
      results.map((movie) => {
        const { title } = movie;
        li.append(`<li>${title}</li>`);
      });
    }
  });
});
