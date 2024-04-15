const loginBtn = document.querySelector("#loginBtn");

loginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  setTimeout(() => {
    window.location.href = "/login";
  }, 500);
});

loginBtn.addEventListener("dblclick", (e) => {
  e.preventDefault();
  window.location.href = "/admin";
  return false;
});

const title = document.querySelector("#title");
title.addEventListener("click", (e) => {
  e.preventDefault();
  setTimeout(() => {
    window.location.href = "/";
  }, 100);
});