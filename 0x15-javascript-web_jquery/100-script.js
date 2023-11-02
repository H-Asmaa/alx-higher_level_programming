#!/usr/bin/node
/* A script that updates the text color of the <header> element to red (#FF0000). */
document.addEventListener('DOMContentLoaded', function () {
  const element = document.querySelector('header');
  element.style.color = '#FF0000';
});
