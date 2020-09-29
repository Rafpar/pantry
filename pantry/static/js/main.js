const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
    $('#message').slideUp();
}, 3000);

// disable product checkboxes when one selected
$(function(){
    $base_checkbox = $("#isBaseProduct");
    $optional_checkbox = $("#isOptionalProduct");
    $custom_checkbox = $("#isCustomProduct");

    $base_checkbox.on('change', function(){
        if($base_checkbox.is(':checked')) {
            $optional_checkbox.attr('disabled', true);
            $custom_checkbox.attr('disabled', true);
        } else {
           $optional_checkbox.attr('disabled', false);
           $custom_checkbox.attr('disabled', false);
        }
    });

    $optional_checkbox.on('change', function(){
        if($optional_checkbox.is(':checked')) {
            $base_checkbox.attr('disabled', true);
            $custom_checkbox.attr('disabled', true);
        } else {
           $base_checkbox.attr('disabled', false);
           $custom_checkbox.attr('disabled', false);
        }
    });

    $custom_checkbox.on('change', function(){
        if($custom_checkbox.is(':checked')) {
            $base_checkbox.attr('disabled', true);
            $optional_checkbox.attr('disabled', true);
        } else {
           $base_checkbox.attr('disabled', false);
           $optional_checkbox.attr('disabled', false);
        }
    });
});

