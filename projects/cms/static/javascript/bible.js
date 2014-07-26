$(document).ready( function() {
    $('#language').change(function() {
        window.location = '/' + $(this).val();
    });

    $('#bible').change(function() {
        window.location = $(this).val();
    });

    $(function() {
        $('#bookmark').click(function() {
            if (window.sidebar && window.sidebar.addPanel) { // Mozilla Firefox Bookmark
                window.sidebar.addPanel(document.title,window.location.href,'');
            } else if(window.external && ('AddFavorite' in window.external)) { // IE Favorite
                window.external.AddFavorite(location.href,document.title);
            } else if(window.opera && window.print) { // Opera Hotlist
                this.title=document.title;
                return true;
            } else { // webkit - safari/chrome
                alert('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != - 1 ? 'Command/Cmd' : 'CTRL') + ' + D to bookmark this page.');
            }
        });
    });

    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "//connect.facebook.net/en_GB/sdk.js#xfbml=1&appId=618903634787090&version=v2.0";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
});
