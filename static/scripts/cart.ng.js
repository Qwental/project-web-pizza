var app = angular.module("myApp", []);
app.controller("CartController", function () {
  var cartCtrl = this;
  cartCtrl.popupOpen = false;
  cartCtrl.productOptionsVisible = false;

  cartCtrl.openCart = function () {
    cartCtrl.popupOpen = true;
    document.body.classList.add("lock");
  };

  cartCtrl.closeCart = function () {
    cartCtrl.popupOpen = false;
    document.body.classList.remove("lock");
  };

  cartCtrl.toggleProductOptions = function () {
    cartCtrl.productOptionsVisible = !cartCtrl.productOptionsVisible;
  };
});
