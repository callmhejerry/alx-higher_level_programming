$("document").ready(() => {
  const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";
  $.get(url, (data, status, xhr) => {
    if (status == "success") {
      const { name } = data;
      $("#character").text(name);
    }
  });
});
