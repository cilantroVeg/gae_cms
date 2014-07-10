(function ($) {
    $("#menu-tab").click(function(){
        if ($("#menu-container").is(':visible')){
            $("#menu-tab").css("marginLeft", "200").animate({
                    marginLeft: "0"
                }, 1000, function() {}
            );
            $("#menu-container").css("marginLeft", "0").animate({
                    marginLeft: -200
                }, 1000, function() {
                    $("#menu-container").css('display', 'none');
                }
            );
        } else{
            $("#menu-tab").css("marginLeft", "0").animate({
                    marginLeft: 200
                }, 1000, function() {}
            );
            $("#menu-container").css('display', 'block');
            $("#menu-container").css("marginLeft", "-200").animate({
                    marginLeft: 0
                }, 1000, function() {

                }
            );
        }
    });
    $(function() {
        $( "#menu" ).menu();
    });
});