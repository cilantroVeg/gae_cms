$(document).ready(function() {
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
            controlNav: false,               //Boolean: Create navigation for paging control of each clide? Note: Leave true for manualControls usage
            directionNav: true             //Boolean: Create navigation for previous/next navigation? (true/false)
        });
        jQuery('.gallery').flexslider({
            controlNav:false,
            directionNav: false
        });
        var navItems = jQuery('#fixed-nav li');
        navItems.find('a').click(function (){
            navItems.removeClass('current');
            this.parentNode.className += ' current';
        });

        initScrollNav({
            nav:'#top-nav a'
        });
        initScrollEnter({
            nav:'#register_link a'
        });
        initialize();

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
    }
);


function initScrollNav(_options){
    var options = jQuery.extend({
        nav:'#nav a',
        animSpeed:750
    }, _options);
    var window = jQuery('html,body');
    var addingHeight = jQuery("#header").outerHeight(true);

    var nav = jQuery(options.nav);;
    nav.each(function (){
        var hold = jQuery(this);
        var block = jQuery(hold.attr('href'));
        if(block.length){
            hold.click(function (){
                var curPos = window.scrollTop();
                var blockPost = block.offset().top - addingHeight;

                window.stop().animate({scrollTop: blockPost},{duration: options.animSpeed});
                return false;
            });
        }
    });
}

function initScrollEnter(_options){
    var options = jQuery.extend({
        nav:'#register_link a',
        animSpeed:750
    }, _options);
    var window = jQuery('html,body');
    var addingHeight = jQuery("#header").outerHeight(true);

    var nav = jQuery(options.nav);;
    nav.each(function (){
        var hold = jQuery(this);
        var block = jQuery(hold.attr('href'));
        if(block.length){
            hold.click(function (){
                var curPos = window.scrollTop();
                var blockPost = block.offset().top - addingHeight;

                window.stop().animate({scrollTop: blockPost},{duration: options.animSpeed});
                return false;
            });
        }
    });
}

function initialize() {
    var latlng = new google.maps.LatLng(47.751676, -122.378773);
    var myOptions = {
        zoom: 12,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);
}

