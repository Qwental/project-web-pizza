// выбираем элемент с классом для дальнейшей работы
const cart = document.querySelector("#cart");
const popup = document.querySelector(".popup");
const popupList = document.querySelector("#popup_product_list");
const popupClose = document.querySelector("#popup_close");
const body = document.body;
const counter = document.getElementById("counter");

const productOptions = document.querySelector("#productOptions");

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

const productOptions_close = document.querySelector(
  '[data-jsaction="productOptions_close"]'
);

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

  /**
   * Создаем элемент для формы
   * @param {*} type
   * @param {*} name
   * @param {*} value
   * @returns
   */
  function createFormElement(type, name, value) {
    const element = document.createElement(type);
    element.name = name;
    if (type === "img") {
      if (value && value.length !== 0) {
        element.src = value;
        element.height = 200;

      } else {
        element.src =
          "https://res.cloudinary.com/practicaldev/image/fetch/s--wen7I4iU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://i.picsum.photos/id/387/200/300.jpg%3Fhmac%3DJlKyfJE4yZ_jxmWXH5sNYl7JdDfP04DOk-hye4p_wtk";
      }
    } else {
      element.innerHTML = value;
    }
    return element;
  }

  /**
   * создание множественного выбора
   * @param {*} name
   * @param {*} value
   * @returns
   */
  function createCheckboxElement(name, value) {
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.name = name;
    checkbox.value = value;
    checkbox.id = `${name}-${value}`;

    const label = document.createElement("label");
    label.htmlFor = checkbox.id;
    label.textContent = value + " рубликов";
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

  function createCsrfInput(token) {
    const tokenInput = document.createElement("input");
    tokenInput.value = token;
    tokenInput.name = "csrfmiddlewaretoken";
    tokenInput.type = "hidden";

    return tokenInput;
  }

  const form = document.getElementById("dynamic-form");

  function createForm(data) {
    const formContainer = document.getElementById("productOptions_form");
    form.textContent = "";
    var token = getCookie("csrftoken");
    const tokenInput = createCsrfInput(token);

    form.appendChild(tokenInput);
    form.setAttribute("data-options-for", id);

    // название и цена выводится всегда
    const nameInput = createFormElement("p", "name", data.name);
    nameInput.setAttribute("data-product-name", data.name);
    const priceInput = createFormElement("small", "price", data.price);
    const imageInput = createFormElement("img", "img-popup", data.img);
    form.appendChild(nameInput);
    const labelForPrice = document.createElement("small");
    labelForPrice.innerText = "Цена: ";
    form.appendChild(labelForPrice);
    form.appendChild(priceInput);
    form.appendChild(imageInput);

    // Проверяем наличие добавок и создаем элементы формы, если они есть
    if (data.options.adds) {
      form.appendChild(document.createElement("hr"));
      var addsLabel = document.createElement("p");
      addsLabel.innerText = "Добавки:";
      form.appendChild(addsLabel);

      data.options.adds.forEach((add) => {
        const { checkbox, label } = createCheckboxElement("add", add);
        form.appendChild(checkbox);
        form.appendChild(label);
        form.appendChild(document.createElement("br"));
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
          form.appendChild(document.createElement("hr"));
          form.appendChild(label);
          form.appendChild(select);
        }
      }
    }

    // ПАМАГИТЕ!!!!!!!!!!!!!!

    formContainer.appendChild(form);
  }

  // Выполнение GET запроса для получения формы
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

      const jsonString = formToJson("dynamic-form");
      console.log("Пользователь выбрал " + jsonString);
      // JSON.stringify(selectedAdds) +

      // добавляем в корзину
      fetch("your-endpoint-url/", {
        method: "POST",
        body: jsonString,
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": token,
        },
      });
    });


}

/**
 * Сохраняем отправленную форму в виде json
 * @param {} formId
 * @param {*} _name
 * @param {*} _id
 * @returns
 */
function formToJson(formId, _name, _id) {
  const form = document.getElementById(formId);
  const formData = new FormData(form);
  const formDataObj = {};
  formDataObj.productName = form.getAttribute("data-product-name");
  formDataObj.productId = form.getAttribute("data-options-for");
  for (let [key, value] of formData.entries()) {
    if (formDataObj.hasOwnProperty(key)) {
      if (Array.isArray(formDataObj[key])) {
        formDataObj[key].push(value);
      } else {
        formDataObj[key] = [formDataObj[key], value];
      }
    } else {
      if (key.startsWith("add")) {
        formDataObj[key] = [value];
      } else {
        formDataObj[key] = value;
      }
    }
  }
  if (!formDataObj.hasOwnProperty("adds")) {
    formDataObj.adds = [];
  }
  return JSON.stringify(formDataObj);
}

// открытие корзинки

const cartBtn = document.getElementById("cart");
cartBtn.addEventListener("click", (event) => {
  event.preventDefault();
  // тут получаем корзину
  fetch();



  
})
