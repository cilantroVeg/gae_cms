$(document).ready( function() {

    $('#language').change(function() {
        window.location = '/' + $(this).val();
    });

    $('#bible').change(function() {
        window.location = $(this).val();
    });

    $('#book').change(function() {
        window.location = $(this).val();
    });

    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&appId=618903634787090&version=v2.0";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

    $("#textsizer-classnames a").textresizer({
        target: "#bible-text, #bible-books",
        type: "cssClass",
        sizes: [
            "small-text",
            "medium-text",
            "large-text",
            "larger-text"
        ],
        selectedIndex: 1
    });

    $("#paragraph-mode").click(function() {
        check_paragraph_preference(true);
    });
    check_paragraph_preference(false);
    hide_favorite_from_non_supported_browsers();
});

function check_paragraph_preference(click) {
    cookie_value = $.cookie('no_breaks');
    if (click)
    {
        if (cookie_value == 'true') {
            $("p").removeClass("no_breaks");
            $("p").addClass("left-text");
            $.cookie('no_breaks', 'false');
            $("#paragraph-mode").removeClass("textresizer-active");
        }else{
            $("p").removeClass("left-text");
            $("p").addClass("no_breaks");
            $.cookie('no_breaks', 'true');
            $("#paragraph-mode").addClass("textresizer-active");
        }
    }
    else
    {
        if (cookie_value == 'true') {
            $("p").removeClass("left-text");
            $("p").addClass("no_breaks");
            $("#paragraph-mode").addClass("textresizer-active");
        }else{
            $("p").removeClass("no_breaks");
            $("p").addClass("left-text");
            $("#paragraph-mode").removeClass("textresizer-active");
        }
    }
}

function hide_favorite_from_non_supported_browsers(){
    if (navigator.userAgent.search("Firefox") < 0) {
        $("#bookmark_list").hide();
    }
}