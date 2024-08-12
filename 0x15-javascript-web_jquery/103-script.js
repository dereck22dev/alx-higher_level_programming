$(document).ready(function () {
  $('INPUT#btn_translate').keypress(function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
    }
  });

  $('#btn_translate ').on('click', function () {

    let languageCode = $('#language_code').val();

    let url = 'https://hellosalut.stefanbohacek.dev/?lang=' + languageCode;

    $.get(url, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
