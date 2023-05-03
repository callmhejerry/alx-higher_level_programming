$("document").ready(() => {
  $("head").ready(() => {
    const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
    $.get(url, (data, status, xhr) => {
      if ((status = "success")) {
        const { hello } = data;
        $("div#hello").text(hello);
      }
    });
  });
});
