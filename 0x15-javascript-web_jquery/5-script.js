#!/usr/bin/nod
/* A script that adds a <li> element to a list when
the user clicks on the tag DIV#add_item. */
/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
