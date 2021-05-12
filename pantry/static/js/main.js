const date = new Date();
const csrftoken = getCookie('csrftoken');
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
    $('#message').slideUp();
}, 3000);

// disable product checkboxes when one selected
$(function () {
    $base_checkbox_add_product = $("#isBaseProduct");
    $optional_checkbox_add_product = $("#isOptionalProduct");
    $custom_checkbox_add_product = $("#isCustomProduct");
    $add_product_button = $("#addProductButton");

    $add_product_button.prop('disabled', true)

    $base_checkbox_add_product.on('change', function () {
        if ($base_checkbox_add_product.is(':checked')) {
            $optional_checkbox_add_product.prop('disabled', true);
            $custom_checkbox_add_product.prop('disabled', true);
            $add_product_button.prop('disabled', false)
        } else {
            $optional_checkbox_add_product.prop('disabled', false);
            $custom_checkbox_add_product.prop('disabled', false);
            $add_product_button.prop('disabled', true)
        }
    });

    $optional_checkbox_add_product.on('change', function () {
        if ($optional_checkbox_add_product.is(':checked')) {
            $base_checkbox_add_product.prop('disabled', true);
            $custom_checkbox_add_product.prop('disabled', true);
            $add_product_button.prop('disabled', false)
        } else {
            $base_checkbox_add_product.prop('disabled', false);
            $custom_checkbox_add_product.prop('disabled', false);
            $add_product_button.prop('disabled', true)
        }
    });

    $custom_checkbox_add_product.on('change', function () {
        if ($custom_checkbox_add_product.is(':checked')) {
            $base_checkbox_add_product.prop('disabled', true);
            $optional_checkbox_add_product.prop('disabled', true);
            $add_product_button.prop('disabled', false)
        } else {
            $base_checkbox_add_product.prop('disabled', false);
            $optional_checkbox_add_product.prop('disabled', false);
            $add_product_button.prop('disabled', true)
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

function clear_add_product_checkboxes() {
    $base_checkbox_add_product.prop('checked', false)
    $base_checkbox_add_product.prop('disabled', false)
    $optional_checkbox_add_product.prop('checked', false)
    $optional_checkbox_add_product.prop('disabled', false)
    $custom_checkbox_add_product.prop('checked', false)
    $custom_checkbox_add_product.prop('disabled', false)
    $add_product_button.prop('disabled', true)
}

// cleanup modals after close
$(document).ready(function () {
    $('.modal').on('hidden.bs.modal', function () {
        $(this).find('form')[0].reset();
    });
});

function remove_row(product_id) {
    $productRow = $("#productRow" + product_id);
    $productName = $productRow.get(0).cells.item(1).textContent;
    if (confirm('Are you sure you want to update ' + $productName + '?')) {
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: 'update/current_amount/' + product_id,
            type: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.updated) {
                    $productRow.remove();
                }
            }
        });
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// filter cards
$(document).ready(function () {
    $("#search-field").on("keyup", function () {
        $(".col-md-6").removeClass('d-none');
        var value = $(this).val()
        $('.card').find('.card-header h4:not(:contains("'+value+'"))').parent().parent().parent().addClass('d-none');
    });
    $('.nav-item').on('click', function () {
        cleanSearchField()
    });
});

function cleanSearchField() {
        var search_field = document.getElementById('search-field');
        search_field.value = '';
        $(".col-md-6").removeClass('d-none');
}
// override contains method to be case insensitive
jQuery.expr[':'].contains = function(a, i, m) {
  return jQuery(a).text().toUpperCase()
      .indexOf(m[3].toUpperCase()) >= 0;
};