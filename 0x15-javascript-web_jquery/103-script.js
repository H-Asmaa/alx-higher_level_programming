#!/usr/bin/
/* A script that fetches and prints how to say “Hello”
depending on the language. */
/* global $ */
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  function validateInput () {
	$('#hello').empty();
    const lang = $('#language_code').val();
    $.get(url + lang, function (data) {
      $('#hello').append(data.hello);
    });
  }
  $('#btn_translate').click(validateInput);
  $('#language_code').on('keydown', function (event) {
    if (event.keyCode === 13) {
      validateInput();
    }
  });
});
