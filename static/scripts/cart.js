// выбираем элемент с классом для дальнейшей работы
const cart = document.querySelector("#cart");
const popup = document.querySelector(".popup");
const popupList = document.querySelector("#popup_product_list");
const popupClose = document.querySelector("#popup_close");
const body = document.body;
const counter = document.getElementById("counter");


// открытие корзинки
cart.addEventListener("click", (e) => {
  e.preventDefault();
  console.log("I am pressed");
  popup.classList.add("popup--open");
  body.classList.add("lock");

  // тут получаем корзину
  fetch();
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

/**
 *
 * @param data
 * @param options
 */
function displayData(data, options) {
  const logDiv = document.getElementById("log");
  let htmlContent = "";
  // Предполагается, что data - это массив объектов
  data.forEach((item, index) => {
    // Преобразование объекта options в строку для отображения

    htmlContent += `<div data-options=${JSON.stringify(options)}>
                       <h2>${item.name}</h2>
                       <p>Цена: ${item.price}</p>
                       <p>Описание: ${item.description}</p>
                       <small>Размер: ${options.data.size}</small>
                       <small>Добавки: ${options.data.toppings}</small>
                       <button class="remove-item" data-index="${index}">Удалить</button>
                     </div>`;
  });

  logDiv.innerHTML = htmlContent;

  document.querySelectorAll(".remove-item").forEach((button) => {
    button.addEventListener("click", function () {
      const index = this.getAttribute("data-index");
      requstDataAll.splice(index, 1);
      this.parentElement.remove();
    });
  });
}


// будет отправлено на бэк
let requstDataAll = [];

