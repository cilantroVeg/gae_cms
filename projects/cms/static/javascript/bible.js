$(document).ready( function() {
    $('#language').change(function() {
        window.location = '/' + $(this).val();
    });
});