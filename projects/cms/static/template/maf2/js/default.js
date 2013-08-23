$(document).ready(function() {
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

