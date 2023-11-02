#!/usr/bin/node
/* A script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello. */
/* global $ */
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data) {
    $('#hello').append(data.hello);
  });
});
