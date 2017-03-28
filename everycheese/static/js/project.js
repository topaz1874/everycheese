/* Project specific Javascript goes here. */

$(document).ready(function() {
    console.log("I am ok!");
    console.log("I am ok ag!");
    console.log("I am ok again!");

      $(".js-create-item").click(function () {
    $.ajax({
      url: '/js/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-item").modal("show");
      },
      success: function (data) {
        $("#modal-item .modal-content").html(data.html_form);
      }
    });
  });
});