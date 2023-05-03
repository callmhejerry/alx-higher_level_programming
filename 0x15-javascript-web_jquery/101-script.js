$("document").ready(() => {
  const newElement = "<li>Item</li>";
  const ulList = $("ul.my_list");

  $("div#add_item").click(() => {
    ulList.append(newElement);
  });

  $("div#remove_item").click(() => {
    $("ul.my_list li:last").remove();
  });

  $("div#clear_list").click(() => {
    ulList.empty();
  });
});
