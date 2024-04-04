// чистый js
// выбираем элемент с классом для дальнейшей работы
const cart = document.querySelector("#cart");
const popup = document.querySelector(".popup");
const popupList = document.querySelector("#popup_product_list");
const popupClose = document.querySelector("#popup_close");
const body = document.body;
const counter = document.getElementById("counter");

// TODO: сделать промежуточный этап: опции

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

// МАССИВ ХРАНИТ ID ПРОДУКТА
var cartArray = [];
var selectedPizzas = [];

// добавляем в корзину
function addToCart(id) {
  var icon = document.getElementById("toggle" + id);
  var cnt = counter;

  // если есть такой продукт в корзине
  if (cartArray.includes(id)) {
    // Удаляем продукт из cartArray
    cartArray = cartArray.filter((item) => item !== id);
    console.log(id + " was removed");
    console.log(cartArray);

    // Находим соответствующий элемент в списке пицц в корзине и удаляем его
    var pizzaItems = document.querySelectorAll("#popup_product_list p");
    pizzaItems.forEach(function (item) {
      if (item.textContent.includes(id)) {
        item.remove();
      }
    });

    // удаляем отображение из корзины
    var pizzaItem = document.querySelector("[data-product-id='" + id + "']");

    if (pizzaItem) {
      popupList.removeChild(pizzaItem);
    } else {
      console.error("Element with data-product-id " + id + " not found");
    }
    // Удаляем соответствующий продукт из массива selectedPizzas
    selectedPizzas = selectedPizzas.filter((pizza) => pizza.id !== id);

    icon.innerHTML = "add";
    cnt.innerHTML = parseInt(cnt.innerHTML) - 1;
  }
  // добавляем в массив
  else {
    cartArray.push(id);
    console.log(id + " was added");
    console.log(cartArray);

    icon.innerHTML = "delete";
    cnt.innerHTML = parseInt(cnt.innerHTML) + 1;

    //аякса
    var xhr = new XMLHttpRequest();
    // открываем запрос по апи
    xhr.open("GET", "/pizza-details?id=" + id, true);
    xhr.onload = function () {
      if (xhr.status === 200) {
        // читаем апи
        var pizza = JSON.parse(xhr.responseText);
        console.log(pizza);
        displayPizza(pizza, id);
        calculateTotalPrice();
      }
    };
    xhr.send();
  }

  calculateTotalPrice();
}

// отображение в корзине
function displayPizza(pizza, id) {
  var icon = document.getElementById("toggle" + id);
  var cnt = counter;

  // == создание карточки товара ==
  var pizzaItem = document.createElement("div");
  pizzaItem.setAttribute("data-product-id", id);
  pizzaItem.innerHTML = "<p>" + pizza.name + " - Цена: " + pizza.price + "</p>";
  popupList.appendChild(pizzaItem);
  // ==============================

  // Добавляем кнопку удаления и вешаем событие клика
  var deleteButton = document.createElement("button");
  deleteButton.setAttribute("id", "deleteBtn");
  deleteButton.innerHTML = "Удалить";
  deleteButton.addEventListener("click", function () {
    popupList.removeChild(pizzaItem);
    // Удаляем соответствующий продукт из массива selectedPizzas
    selectedPizzas = selectedPizzas.filter((item) => item.id !== id);
    calculateTotalPrice(); // Пересчитываем общую сумму после удаления продукта из корзины
    icon.innerHTML = "add";
    cnt.innerHTML = parseInt(cnt.innerHTML) - 1;
  });
  pizzaItem.appendChild(deleteButton); // Добавляем кнопку удаления к блоку пиццы
  selectedPizzas.push({ id: id, name: pizza.name, price: pizza.price });
}

// итог согласно сумме цен
function calculateTotalPrice() {
  var totalPrice = 0;
  selectedPizzas.forEach(function (pizza) {
    totalPrice += parseInt(pizza.price);
  });
  document.getElementById("popup_cost").innerHTML = totalPrice;
}
