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

    $baseProductsTab = $("#baseProducts");
    $optionalProductsTab = $("#optionalProducts");
    $customProductsTab = $("#customProducts");



    $base_checkbox.on('change', function () {
        if ($base_checkbox.is(':checked') || $optional_checkbox.is(':checked') || $custom_checkbox.is(':checked')) {
            $get_shopping_list_buton.prop('disabled', false);
        } else {
            $get_shopping_list_buton.prop('disabled', true);
        }
    });

    $optional_checkbox.on('change', function () {
        if ($base_checkbox.is(':checked') || $optional_checkbox.is(':checked') || $custom_checkbox.is(':checked')) {
            $get_shopping_list_buton.prop('disabled', false);
        } else {
            $get_shopping_list_buton.prop('disabled', true);
        }
    });

    $custom_checkbox.on('change', function () {
        if ($base_checkbox.is(':checked') || $optional_checkbox.is(':checked') || $custom_checkbox.is(':checked')) {
            $get_shopping_list_buton.prop('disabled', false);
        } else {
            $get_shopping_list_buton.prop('disabled', true);
        }
    });


});

document.addEventListener("DOMContentLoaded", function (event) {
    var scrollpos = sessionStorage.getItem('scrollpos');

    if (scrollpos) {
        window.scrollTo(0, scrollpos);
        sessionStorage.removeItem('scrollpos');
    }
});

window.addEventListener("pagehide", function (e) {
    sessionStorage.setItem('scrollpos', window.scrollY);
});

function set_default_checkbox() {

    $active_tab = $('.nav-tabs .active')
    $active_tab_id = $active_tab.get(0).id

    if ($active_tab_id === "base-products-tab") {
        $base_checkbox.prop('checked', true)
    } else {
        $base_checkbox.prop('checked', false)
    }
    if ($active_tab_id === "optional-products-tab") {
        $optional_checkbox.prop('checked', true)
    } else {
        $optional_checkbox.prop('checked', false)
    }
    if ($active_tab_id === "custom-products-tab") {
        $custom_checkbox.prop('checked', true)
    } else {
        $custom_checkbox.prop('checked', false)
    }
    $get_shopping_list_buton.prop('disabled', false);
}

function clear_checkboxes() {
    $base_checkbox.prop('checked', false)
    $optional_checkbox.prop('checked', false)
    $custom_checkbox.prop('checked', false)
}

// cleanup modals after close
$(document).ready(function() {
    $('.modal').on('hidden.bs.modal', function(){
        $(this).find('form')[0].reset();
     });
});