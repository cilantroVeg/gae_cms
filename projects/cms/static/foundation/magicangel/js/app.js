$(document).foundation();

$( document ).ready(function() {
    $('#slide-maf').slick({
        autoplay:true,
        autoplaySpeed:5000,
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots:true,
        arrows:true,
        initialSlide:1,
        mobileFirst:true,
    });
    $('#slide-maf').show();
});

function scroll_to_anchor(anchor_id){
    var tag = $("#"+anchor_id+"");
    $('html,body').animate({scrollTop: tag.offset().top - 100},'slow');
}

function scroll_to_anchor(anchor_id, offset_value){
    var tag = $("#"+anchor_id+"");
    $('html,body').animate({scrollTop: tag.offset().top - offset_value},'slow');
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

 $(window).bind("load", function () {
    var footer = $("#footer");
    var pos = footer.position();
    var height = $(window).height();
    height = height - pos.top;
    height = height - footer.height();
    if (height > 0) {
        footer.css({
            'margin-top': height + 'px'
        });
    }
});