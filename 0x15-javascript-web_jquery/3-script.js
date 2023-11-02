#!/usr/bin/node
/* A script that adds a class to an element by clique. */
/* global $ */
$(document).ready(function () {
	$('#red_header').click(function () {
	  $("header").addClass('red');
	});
  });
