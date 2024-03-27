// чистый js
// выбираем элемент с классом для дальнейшей работы
const cart = document.querySelector("#cart");
const popup = document.querySelector(".popup");
const popupClose = document.querySelector("#popup_close");
const body = document.body;

// открытия корзины
cart.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("I am pressed");
  popup.classList.add("popup--open");
  body.classList.add("lock");
});

// закрытие корзины
popupClose.addEventListener("click", (e) => {
  e.preventDefault();
  popup.classList.remove("popup--open");
  body.classList.remove("lock");
});
// // jquery
// // открытие корзины
// $("#cart").click((e) => {
//   e.preventDefault();
//   console.log("I am pressed");
//   $(".popup").addClass("popup--open");
//   $("body").addClass("lock");
// });

// // закрытие корзины
// $("#popup_close").click((e) => {
//   e.preventDefault();
//   $(".popup").removeClass("popup--open");
//   $("body").removeClass("lock");
// });