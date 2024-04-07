// чистый js
// выбираем элемент с классом для дальнейшей работы
const cart = document.querySelector("#cart");
const popup = document.querySelector(".popup");
const popupList = document.querySelector("#popup_product_list");
const popupClose = document.querySelector("#popup_close");
const body = document.body;
const counter = document.getElementById("counter");

const productOptions = document.querySelector("#productOptions");

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
// function addToCart(id) {
//   var icon = document.getElementById("toggle" + id);
//   var cnt = counter;

//   // если есть такой продукт в корзине
//   if (cartArray.includes(id)) {
//     // Удаляем продукт из cartArray
//     cartArray = cartArray.filter((item) => item !== id);
//     console.log(id + " was removed");
//     console.log(cartArray);

//     // Находим соответствующий элемент в списке пицц в корзине и удаляем его
//     var pizzaItems = document.querySelectorAll("#popup_product_list p");
//     pizzaItems.forEach(function (item) {
//       if (item.textContent.includes(id)) {
//         item.remove();
//       }
//     });

//     // удаляем отображение из корзины
//     var pizzaItem = document.querySelector("[data-product-id='" + id + "']");

//     if (pizzaItem) {
//       popupList.removeChild(pizzaItem);
//     } else {
//       console.error("Element with data-product-id " + id + " not found");
//     }
//     // Удаляем соответствующий продукт из массива selectedPizzas
//     selectedPizzas = selectedPizzas.filter((pizza) => pizza.id !== id);

//     icon.innerHTML = "add";
//     cnt.innerHTML = parseInt(cnt.innerHTML) - 1;
//   }
//   // добавляем в массив
//   else {
//     cartArray.push(id);
//     console.log(id + " was added");
//     console.log(cartArray);

//     icon.innerHTML = "delete";
//     cnt.innerHTML = parseInt(cnt.innerHTML) + 1;

//     //аякса
//     var xhr = new XMLHttpRequest();
//     // открываем запрос по апи
//     xhr.open("GET", "/pizza-details?id=" + id, true);
//     xhr.onload = function () {
//       if (xhr.status === 200) {
//         // читаем апи
//         var pizza = JSON.parse(xhr.responseText);
//         console.log(pizza);
//         displayPizza(pizza, id);
//         calculateTotalPrice();
//       }
//     };
//     xhr.send();
//   }

//   calculateTotalPrice();
// }

// // отображение в корзине
// function displayPizza(pizza, id) {
//   var icon = document.getElementById("toggle" + id);
//   var cnt = counter;

//   // == создание карточки товара ==
//   var pizzaItem = document.createElement("div");
//   pizzaItem.setAttribute("data-product-id", id);
//   pizzaItem.innerHTML = "<p>" + pizza.name + " - Цена: " + pizza.price + "</p>";
//   popupList.appendChild(pizzaItem);
//   // ==============================

//   // Добавляем кнопку удаления и вешаем событие клика
//   var deleteButton = document.createElement("button");
//   deleteButton.setAttribute("id", "deleteBtn");
//   deleteButton.innerHTML = "Удалить";
//   deleteButton.addEventListener("click", function () {
//     popupList.removeChild(pizzaItem);
//     // Удаляем соответствующий продукт из массива selectedPizzas
//     selectedPizzas = selectedPizzas.filter((item) => item.id !== id);
//     calculateTotalPrice(); // Пересчитываем общую сумму после удаления продукта из корзины
//     icon.innerHTML = "add";
//     cnt.innerHTML = parseInt(cnt.innerHTML) - 1;
//   });
//   pizzaItem.appendChild(deleteButton); // Добавляем кнопку удаления к блоку пиццы
//   selectedPizzas.push({ id: id, name: pizza.name, price: pizza.price });
// }

// // итог согласно сумме цен
// function calculateTotalPrice() {
//   var totalPrice = 0;
//   selectedPizzas.forEach(function (pizza) {
//     totalPrice += parseInt(pizza.price);
//   });
//   document.getElementById("popup_cost").innerHTML = totalPrice;
// }

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

// получаем csrftoken
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// будет отправлено на бэк
let requstDataAll = [];
function addToCartp(id) {
  var element = document.getElementById("productOptions");
  element.classList.remove("hide");
  element.classList.add("show");
  element.setAttribute("data-product-id-menu", id);
  const csrftoken = getCookie("csrftoken");

  function createFormElement(type, name, value) {
    const element = document.createElement(type);
    element.name = name;
    element.innerHTML = value;
    return element;
  }

  function createCheckboxElement(name, value) {
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.name = name;
    checkbox.value = value;
    checkbox.id = `${name}-${value}`;

    const label = document.createElement("label");
    label.htmlFor = checkbox.id;
    label.textContent = value + " рубликов\n";
    return { checkbox, label };
  }

  /**
   * Создает элемент-выбор
   * @param {*} name
   * @param {*} options
   * @returns
   */
  function createSelectElement(name, options) {
    const select = document.createElement("select");
    select.name = name;
    if (options != null) {
      options.forEach((option) => {
        const optionElement = document.createElement("option");
        if (option.value != null) {
          optionElement.value = option.value;
          optionElement.textContent = option.value;
          select.appendChild(optionElement);
        }
      });
    }
    return select;
  }
  // const form = document.createElement("form");
  // form.id = "dynamic-form";

  const form = document.getElementById("dynamic-form");

  function createForm(data) {
    const formContainer = document.getElementById("productOptions");
    form.textContent = "";
    // formContainer.textContent = "";

    form.setAttribute("data-optins-for", id);

    // название и цена выводится всегда
    const nameInput = createFormElement("p", "name", data.name);
    const priceInput = createFormElement("small", "price", data.price);
    form.appendChild(nameInput);
    form.appendChild(priceInput);

    // Проверяем наличие добавок и создаем элементы формы, если они есть
    if (data.options.adds) {
      var addsLabel = document.createElement("p");
      addsLabel.innerText = "Добавки:";
      form.appendChild(addsLabel);

      data.options.adds.forEach((add) => {
        const { checkbox, label } = createCheckboxElement("add", add);
        form.appendChild(checkbox);
        form.appendChild(label);
      });
    }

    for (const optionName in data.options) {
      // убираем добавки, ведь они уже были выше
      if (data.options.hasOwnProperty(optionName) && optionName !== "adds") {
        const options = data.options[optionName];
        if (options && options.length > 0 && optionName !== "adds") {
          const select = createSelectElement(optionName, options);
          var label = document.createElement("p");
          label.innerText = optionName + ":"; // Используем имя как лэйбл
          form.appendChild(label);
          form.appendChild(select);
        }
      }
    }

    // ПАМАГИТЕ!!!!!!!!!!!!!!

    const submitButton = document.createElement("button");
    submitButton.type = "submit";
    submitButton.textContent = "Отправить";
    form.appendChild(submitButton);

    formContainer.appendChild(form);
  }

  // Выполнение GET запроса
  fetch(`api/?id=${id}`)
    .then((response) => response.json())
    .then((data) => createForm(data))
    .catch((error) => console.error("Ошибка:", error));

  // отправка
  +document
    .getElementById("dynamic-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();

      var selectedAdds = Array.from(
        document.querySelectorAll('#dynamic-form input[name="add"]:checked')
      ).map(function (checkbox) {
        return checkbox.value;
      });


      // Формируем тело запроса
      const requestBody = {
        adds: selectedAdds,
      };

      console.log("Выбранные добавки:", requestBody);

      // requstDataAll.push({
      //   id: id,
      //   data: {
      //     toppings: selectedToppings,
      //   },
      // });
      //
      // console.log(requstDataAll);

      const jsonString = formToJson('dynamic-form');
      console.log("Пользователь выбрал " + jsonString);
      // displayData(id, jsonString);


      // НЕКИЙ ЗАПРОС
      /**
       * отпраялем id и опции, возвращаем -- название, описание, цену
       */
      // fetch("/your-endpoint-url/", {
      //   method: "POST",
      //   headers: {
      //     "Content-Type": "application/json",
      //     "X-CSRFToken": csrftoken,
      //   },
      //   body: JSON.stringify({ items: requestBody }),
      // })
      //   .then((response) => response.json())
      //   .then((data) => {
      //     // Обработка ответа от сервера
      //     displayData(data, {
      //       data: {
      //         size: selectedSize,
      //         toppings: selectedToppings,
      //       },
      //     });
      //     console.log(data);
      //     // Здесь можно добавить код для обновления интерфейса с полученными данными
      //   })
      //   .catch((error) => {
      //     console.error("Ошибка:", error);
      //   });
    });
}
const productOptions_close = document.querySelector("#productOptions_close");

productOptions_close.addEventListener("click", (e) => {
  e.preventDefault();
  var element = document.getElementById("productOptions");
  element.classList.remove("show");
  element.classList.add("hide");
});

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
  }, 500);
});

function formToJson(formId) {
  const form = document.getElementById(formId);
  const formData = new FormData(form);
  const formDataObj = {};

  for (let [key, value] of formData.entries()) {
    if (formDataObj.hasOwnProperty(key)) {
      if (Array.isArray(formDataObj[key])) {
        formDataObj[key].push(value);
      } else {
        formDataObj[key] = [formDataObj[key], value];
      }
    } else {
      if (key.startsWith('add')) {
        formDataObj[key] = [value];
      } else {
        formDataObj[key] = value;
      }
    }
  }

  // Convert the JavaScript object to a JSON string
  return JSON.stringify(formDataObj);
}


// TODO: мувнуть это все нахуй на нормальный фреймворк