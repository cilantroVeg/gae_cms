$( document ).ready(function() {
    $( "#search" ).autocomplete({
        source: availableTags
    });
});

function scroll_to_anchor(anchor_id){
    var tag = $("#"+anchor_id+"");
    $('html,body').animate({scrollTop: tag.offset().top},'slow');
}