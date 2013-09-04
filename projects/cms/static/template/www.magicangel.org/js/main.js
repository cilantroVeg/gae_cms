(function ($) {
// VERTICALLY ALIGN FUNCTION
    $.fn.vAlign = function() {
        return this.each(function(i){
            var ah = $(this).height();
            var ph = $(this).parent().height();
            var mh = Math.ceil((ph-ah) / 2);
            $(this).css('padding-top', mh);
        });
    };
})(jQuery);
$(document).ready(function(){
    var win_h = $(window).height();
    function setHeight(){
        $('.home > .hero').css({height:win_h});
        $(".vcenter").vAlign();
    }

    setHeight();
    /*$(".slogan h1").slabText({
     "viewportBreakpoint":300
     });*/

    $(window).bind('resize',function() {
        setHeight();
    });

    $('#top-nav').onePageNav({

        currentClass: 'current',
        changeHash: false,
        scrollSpeed: 750,
        scrollOffset: 81,
        scrollThreshold: 0.5,
        filter: ':not(.external)',
        begin: function() {
            //I get fired when the animation is starting
        },
        end: function() {
            //I get fired when the animation is ending
        },
        scrollChange: function() {
            //I get fired when you enter a section and I pass the list item of the section
        }
    });

    $('#nav-button').click(function(){
        $top_nav = $('#top-nav');
        if($top_nav.is(':hidden')){
            $top_nav.slideDown("slow");
        }else{
            $top_nav.slideUp();
        }
    })

    $('.flexslider').flexslider({
        controlNav:true,
        direction: "horizontal",        //String: Select the sliding direction, "horizontal" or "vertical"
        reverse: false,                 //{NEW} Boolean: Reverse the animation direction
        animationLoop: true,             //Boolean: Should the animation loop? If false, directionNav will received "disable" classes at either end
        smoothHeight: false,            //{NEW} Boolean: Allow height of the slider to animate smoothly in horizontal mode
        startAt: 0,                     //Integer: The slide that the slider should start on. Array notation (0 = first slide)
        slideshow: true,                //Boolean: Animate slider automatically
        slideshowSpeed: 7000,           //Integer: Set the speed of the slideshow cycling, in milliseconds
        animationSpeed: 600,            //Integer: Set the speed of animations, in milliseconds
        initDelay: 0,                   //{NEW} Integer: Set an initialization delay, in milliseconds
        randomize: false,               //Boolean: Randomize slide order
        pauseOnAction: true,            //Boolean: Pause the slideshow when interacting with control elements, highly recommended.
        pauseOnHover: true,            //Boolean: Pause the slideshow when hovering over slider, then resume when no longer hovering
        useCSS: true,                   //{NEW} Boolean: Slider will use CSS3 transitions if available
        touch: true,                    //{NEW} Boolean: Allow touch swipe navigation of the slider on touch-enabled devices
        video: false,                   //{NEW} Boolean: If using video in the slider, will prevent CSS3 3D Transforms to avoid graphical glitches
        controlNav: true,               //Boolean: Create navigation for paging control of each clide? Note: Leave true for manualControls usage
        directionNav: true             //Boolean: Create navigation for previous/next navigation? (true/false)
    });
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