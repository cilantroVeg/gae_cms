$( document ).ready(function() {
    $( "#search" ).autocomplete({
        source: availableTags
    });
    $( "#search" ).focus(function() {
        $("#feedback").hide("highlight", {}, 200);
    });
});

function scroll_to_anchor(anchor_id){
    var tag = $("#"+anchor_id+"");
    $('html,body').animate({scrollTop: tag.offset().top},'slow');
}

function scroll_to_anchor_and_show_tip(anchor_id){
    var tag = $("#"+anchor_id+"");
    scroll_to_anchor(anchor_id);
    tag.effect("highlight", {}, 1500);
}

function search_results(search){
    // Check if slug is in availableTags
    var tag_exists = false
    for (index = 0; index < availableTags.length; ++index) {
        if (availableTags[index].value == search){
            tag_exists = true;
            console.log(availableTags[index]);
        }
    }
    if (tag_exists){
        $("#feedback").hide("highlight", {}, 1500);
        scroll_to_anchor_and_show_tip(search);
    }else {
        var html = '<div data-alert class="alert-box warning">'+search+' Not Found <a href="#" class="close">×</a></div>';
        $("#feedback").html(html);
        $("#feedback").show("highlight", {}, 1500);
    }
}