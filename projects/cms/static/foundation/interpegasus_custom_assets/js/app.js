$(document).foundation();

$( document ).ready(function() {
    $('#slide-ip').slick({
        autoplay:false,
        autoplaySpeed:5000,
        infinite: true,
        slidesToShow: 2,
        slidesToScroll: 2,
        dots:false,
        arrows:false,
        initialSlide:1,
        mobileFirst:true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }]
    });
    $('#slide-ip').show();

    $('#slide-news').slick({
        autoplay:true,
        autoplaySpeed:5000,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        dots:false,
        arrows:true,
        initialSlide:1,
        mobileFirst:true,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 3
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 2
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }]
    });
    $('#slide-news').show();

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