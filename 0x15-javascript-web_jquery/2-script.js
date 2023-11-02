#!/usr/bin/no
/* A script that changes the color of an element by id. */
/* global $ */
$(document).ready(function () {
  $('#red_header').click(function () {
    $(this).css('color', '#FF0000');
  });
});
