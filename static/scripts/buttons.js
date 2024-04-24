const loginBtn = document.querySelector("#loginBtn");

loginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  setTimeout(() => {
    window.location.href = "/user/login";
  }, 500);
});

const logoutBtn = document.querySelector("#logoutBtn");

logoutBtn.addEventListener("click", (e) => {
  e.preventDefault();
  setTimeout(() => {
    window.location.href = "/user/logout";
  }, 500);
});

const regBtn = document.querySelector("#regBtn");

regBtn.addEventListener("click", (e) => {
  e.preventDefault();
  setTimeout(() => {
    window.location.href = "/user/registration";
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


* {
    box-sizing: border-box;
}

* {
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Montserrat', sans-serif;
}

.block {
    width: 600px;
    height: 200px;
    border-radius: 20px;
    background-image: url(images/pizza1.jpg);
    background-size: cover;
    display: flex;
    flex-wrap: wrap;
    justify-content: left;
}

.block span {
    font-size: 26px;
    color: white;
    margin: 10px 289px 0px 20px;
    letter-spacing: 3px;
}

.btn {
    width: 130px;
    height: 45px;
    border-radius: 12px;
    filter: drop-shadow(0px 2px 2.5px rgba(33, 33, 33, 0.35));
    background-color: #fd9824;
    line-height: 45px;

    color: white;
    font-size: 18px;
    font-weight: 700;
    text-align: center;
    display: inline-block;
    text-decoration: none;
    letter-spacing: 1px;
    margin-left: 20px;
    margin-bottom: 10px;
}

.btn:hover {
    background-color: #388cfa;
}