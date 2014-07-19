$(document).ready( function() {
    $('#language').change(function() {
        window.location = '/' + $(this).val();
    });
});

function set_selected_attribute(current_language) {
    $("#language").val(current_language);
}