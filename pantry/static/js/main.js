const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
    $('#message').slideUp();
}, 3000);

// disable product checkboxes when one selected
$(function () {
    $base_checkbox = $("#isBaseProduct");
    $optional_checkbox = $("#isOptionalProduct");
    $custom_checkbox = $("#isCustomProduct");

    $base_checkbox.on('change', function () {
        if ($base_checkbox.is(':checked')) {
            $optional_checkbox.attr('disabled', true);
            $custom_checkbox.attr('disabled', true);
        } else {
            $optional_checkbox.attr('disabled', false);
            $custom_checkbox.attr('disabled', false);
        }
    });

    $optional_checkbox.on('change', function () {
        if ($optional_checkbox.is(':checked')) {
            $base_checkbox.attr('disabled', true);
            $custom_checkbox.attr('disabled', true);
        } else {
            $base_checkbox.attr('disabled', false);
            $custom_checkbox.attr('disabled', false);
        }
    });

    $custom_checkbox.on('change', function () {
        if ($custom_checkbox.is(':checked')) {
            $base_checkbox.attr('disabled', true);
            $optional_checkbox.attr('disabled', true);
        } else {
            $base_checkbox.attr('disabled', false);
            $optional_checkbox.attr('disabled', false);
        }
    });
});

// enable get shopping list button
$(function () {
    $base_checkbox = $("#isBaseProductShoppingList");
    $optional_checkbox = $("#isOptionalProductShoppingList");
    $custom_checkbox = $("#isCustomProductShoppingList");
    $get_shopping_list_buton = $("#getShoppingList");

    $base_checkbox.on('change', function ()
    {
        if ($base_checkbox.is(':checked') || $optional_checkbox.is(':checked') || $custom_checkbox.is(':checked')) {
            $get_shopping_list_buton.attr('disabled', false);
        } else {
            $get_shopping_list_buton.attr('disabled', true);
        }
    });

    $optional_checkbox.on('change', function ()
    {
        if ($base_checkbox.is(':checked') || $optional_checkbox.is(':checked') || $custom_checkbox.is(':checked')) {
            $get_shopping_list_buton.attr('disabled', false);
        } else {
            $get_shopping_list_buton.attr('disabled', true);
        }
    });

    $custom_checkbox.on('change', function ()
    {
        if ($base_checkbox.is(':checked') || $optional_checkbox.is(':checked') || $custom_checkbox.is(':checked')) {
            $get_shopping_list_buton.attr('disabled', false);
        } else {
            $get_shopping_list_buton.attr('disabled', true);
        }
    });





});
