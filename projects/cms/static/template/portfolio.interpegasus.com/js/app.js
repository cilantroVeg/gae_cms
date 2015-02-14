function scroll_to_anchor(anchor_id){
    alert(1);
    var tag = $("#"+anchor_id+"");
    $('html,body').animate({scrollTop: tag.offset().top},'slow');
}