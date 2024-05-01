// Когда html документ готов (прорисован)
$(document).ready(function () {
    // Универсальная функция для удаления товара из корзины
    function removeFromCart(cartID, removeUrl) {
        $.ajax({
            type: "POST",
            url: removeUrl,
            data: {
                cart_id: cartID,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function(data) {
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function(data) {
                console.log("Ошибка при удалении товара из корзины");
            }
        });
    }

    // Ловим собыитие клика по кнопке удалить товар из корзины
    $(document).on("click", ".remove-from-cart", function(e) {
        e.preventDefault();
        var cartID = $(this).data("cart-id");
        var removeUrl = $(this).attr("href");

        removeFromCart(cartID, removeUrl);
    });

    // Обработчик для уменьшения количества товара
    $(document).on("click", ".decrement", function () {
        var url = $(this).data("cart-change-url");
        var cartID = $(this).data("cart-id");
        var $input = $(this).closest('.input-group').find('.number');
        var currentValue = parseInt($input.val());

        if (currentValue > 1) {
            // делаем в поле -1
            $input.val(currentValue - 1);
            updateCart(cartID, currentValue - 1, -1, url);
        } else if (currentValue === 1) {
            // var removeUrl = $(this).closest('.cart-item').find('.remove-from-cart').attr('href');
            removeFromCart(cartID, "/cart/cart_remove/");
        }
    });

    // Обработчик события для увеличения значения
    $(document).on("click", ".increment", function () {
        // Берем ссылку на контроллер django из атрибута data-cart-change-url
        var url = $(this).data("cart-change-url");
        // Берем id корзины из атрибута data-cart-id
        var cartID = $(this).data("cart-id");
        // Ищем ближайшеий input с количеством 
        var $input = $(this).closest('.input-group').find('.number');
        // Берем значение количества товара
        var currentValue = parseInt($input.val());
        // делаем в поле +1
        $input.val(currentValue + 1);

        // Запускаем функцию определенную ниже
        // с аргументами (id карты, новое количество, количество уменьшилось или прибавилось, url)
        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                // Меняем содержимое корзины
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину: ", data);
            },
        });
    }
});