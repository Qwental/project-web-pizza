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

function addToCartp(id) {
  const element = document.getElementById("productOptions");
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
    // создаем инпут-чексбокс
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.name = name;
    checkbox.value = value;
    checkbox.id = `${name}-${value}`;
    checkbox.setAttribute("data-value-checkbox", value.split(":")[1])
    checkbox.className = "form-check-input";

    // Создаем label для чекбокса
    const label = document.createElement("label");
    label.htmlFor = checkbox.id;
    label.className = "form-check-label";
    label.textContent = value + " рубликов";

    // Создаем вспомогательный div для чекбокса и метки
    const container = document.createElement("div");
    container.className = "form-check";
    container.appendChild(checkbox);
    container.appendChild(label);

    return { container };
  }

  /**
   * Создает элемент-выбор
   * @param {*} name
   * @param {*} options
   * @returns
   */
  function createSelectElement(name, options) {
    // cоздаем вспомогательный div
    const radioGroup = document.createElement("div");
    radioGroup.className = "btn-group";
    radioGroup.setAttribute("data-toggle", "buttons");
    radioGroup.setAttribute("data-options", options);

    options.forEach((option, index) => {
      const radioButton = document.createElement("label");
      radioButton.className = "btn btn-secondary";

      // создаем вариант
      const input = document.createElement("input");
      input.type = "radio";
      input.name = name;
      input.id = `${name}-${index}`;
      input.className = "btn-check";
      input.autocomplete = "off";
      input.setAttribute("data-value-radio", option.price)


      // проверка нулевого дня
      if (option.value != null) {
        input.value = option.value;
      }

      radioButton.appendChild(input);

      const span = document.createElement("span");
      span.textContent = option.value;
      radioButton.appendChild(span);

      radioGroup.appendChild(radioButton);
    });

    // делаем логику клику
    radioGroup.addEventListener('click', function (event) {
      if (event.target.tagName === 'LABEL') {
        this.querySelectorAll('.btn.active').forEach(function (activeBtn) {
          activeBtn.classList.remove('active');
        });
        event.target.classList.add('active');
      }

    });

    return radioGroup;
  }

  function createCsrfInput(token) {
    const tokenInput = document.createElement("input");
    tokenInput.value = token;
    tokenInput.name = "csrfmiddlewaretoken";
    tokenInput.type = "hidden";

    return tokenInput;
  }

  const form = document.getElementById("dynamic-form");

  const productOptions_close = document.querySelector(
    '[data-jsaction="productOptions_close"]'
  );

  productOptions_close.addEventListener("click", (e) => {
    e.preventDefault();
    const element = document.getElementById("productOptions");
    element.classList.remove("show");
    element.classList.add("hide");
    form.textContent = "";
  });

  function createForm(data, _basePrice, price) {
    /**
     * Заранее инициализируем итоговую цену
     */
    const finalPriceInput = createFormElement("p", "price", price);

    /**
     * Работаем с DOM при обновлении уены
     * @param {*} newPrice
     */
    function updateFinalPriceInput(newPrice) {
      finalPriceInput.textContent = newPrice;
    }

    const formContainer = document.getElementById("productOptions_form");

    const token = getCookie("csrftoken");
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
      const addsLabel = document.createElement("p");
      addsLabel.innerText = "Добавки:";
      form.appendChild(addsLabel);

      data.options.adds.forEach((add) => {
        const { container } = createCheckboxElement("add", add);
        form.appendChild(container);
        form.appendChild(document.createElement("br"));
      });
    }

    for (const optionName in data.options) {
      // убираем добавки, ведь они уже были выше
      if (data.options.hasOwnProperty(optionName) && optionName !== "adds") {
        const options = data.options[optionName];
        if (options && options.length > 0 && optionName !== "adds") {
          const select = createSelectElement(optionName, options);
          const label = document.createElement("p");

          label.innerText = optionName + ":";
          form.appendChild(document.createElement("hr"));
          form.appendChild(label);
          form.appendChild(select);
        }
      }
    }

    /**
     * Логика обработки смены цены при выборе опций
     */
    let previousCheckedRadio = null;

    form.addEventListener('change', function (event) {
      if (event.target.type === 'checkbox') {
        const checkbox = event.target;
        const checkboxValue = parseInt(checkbox.getAttribute('data-value-checkbox'));
        if (checkbox.checked) {
          price += checkboxValue;
          updateFinalPriceInput(price);
        } else {
          price -= checkboxValue;
          updateFinalPriceInput(price);
        }
      }
      else if (event.target.type === 'radio') {
        const checkedRadio = event.target;
        if (checkedRadio) {
          const radioValue = parseFloat(checkedRadio.getAttribute('data-value-radio'));
          // Не будет работать в случае: сначала выбераем S, Тесто Тонкое, затем - Толстое, далее - Тонкое, в конце - M -- цена не изменилась, стэк переполнен, т.к. предыдущий радио хранится только один
          // Исправлять или сделать условностью? Либо поменять стратегию подсчета цены?.. Амелия?
          if (previousCheckedRadio && previousCheckedRadio.name === checkedRadio.name) {
            const previousRadioValue = parseFloat(previousCheckedRadio.getAttribute('data-value-radio'));
            price /= previousRadioValue;
          }
          price *= radioValue;
          updateFinalPriceInput(price);

          previousCheckedRadio = checkedRadio;
        }
      }

      console.log(price);
    });
    // ПАМАГИТЕ!!!!!!!!!!!!!!


    const labelForfinalPriceInput = document.createElement("p");
    labelForfinalPriceInput.innerText = "Итого: ";
    form.appendChild(document.createElement("hr"));
    form.appendChild(labelForfinalPriceInput);
    form.appendChild(finalPriceInput);
    formContainer.appendChild(form);

  }

  let basePrice = 0;
  let price = 0;
  // Выполнение GET запроса для получения формы
  fetch(`api/?id=${id}`)
    .then((response) => response.json())
    .then((data) => {
      basePrice = price = parseInt(data.price);
      createForm(data, basePrice, price);
    })
    .catch((error) => console.error("Ошибка:", error));


  console.log(price)
    // отправка
    + document
      .getElementById("dynamic-form")
      .addEventListener("submit", function (event) {
        event.preventDefault();

        const jsonString = formToJson("dynamic-form", price);
        console.log("Пользователь выбрал " + jsonString);
        const jsonObject = JSON.parse(jsonString);
        const token = getCookie("csrftoken");

        // добавляем в корзину
        if (jsonObject.options && typeof jsonObject.options === 'object' && Object.keys(jsonObject.options).length >= 1) {
          fetch("cart/cart_add/", {
            method: "POST",
            body: jsonString,
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": token,
            },
          }).then(response => response.json())
            .then(data => {
              if (data.message === "Товар добавлен в корзину") {
                $('#successModal').modal('show');
              }
              else {
                $('#errorModal').modal('show');
              }
            })
            .catch(error => console.error('Error:', error));
        }
        else {
          $('#netOptions').modal('show');
        }

      });
}

/**
 * Сохраняем отправленную форму в виде json
 * @param {string} formId
 * @param {*} price
 * @param {*} _id
 * @returns
 */
function formToJson(formId, price, _id) {
  const form = document.getElementById(formId);
  const formData = new FormData(form);
  const formDataObj = {};

  // formDataObj.productName = form.getAttribute("data-product-name");

  formDataObj.productId = form.getAttribute("data-options-for");
  formDataObj.options = {};
  let optionsBlock = formDataObj.options;
  for (let [key, value] of formData.entries()) {
    if (key === 'csrfmiddlewaretoken') continue;
    if (formDataObj.hasOwnProperty(key)) {
      if (Array.isArray(formDataObj[key])) {
        optionsBlock[key].push(value);
      } else {
        optionsBlock[key] = [optionsBlock[key], value];
      }
    } else {
      if (key.startsWith("add")) {
        optionsBlock[key] = [value];
      } else {
        optionsBlock[key] = value;
      }
    }
  }
  if (!optionsBlock.hasOwnProperty("add")) {
    optionsBlock.add = [];
  }
  formDataObj['price'] = price;
  return JSON.stringify(formDataObj);
}
