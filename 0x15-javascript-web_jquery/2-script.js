#!/usr/bin/node
/* A script that changes the color of an element by id. */
/* global $ */
$(document).ready(function () {
  $('#red_header').click(function () {
    $("header").css('color', '#FF0000');
  });
});
