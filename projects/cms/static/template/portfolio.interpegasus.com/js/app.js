$( document ).ready(function() {
    $( "#search" ).autocomplete({
        source: availableTags,
        response : function(event, ui) {
            if (!ui.content.length){
                ui.content.push({ label: "No Results", value: "No Results" });
            }
            console.log(ui.length);
        }
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
        var html = '<div data-alert class="alert-box warning">The search did not return an exact match.</a></div>';
        $("#feedback").html(html);
        $("#feedback").fadeIn(500);
        $("#feedback").fadeOut(3000);

    }
}