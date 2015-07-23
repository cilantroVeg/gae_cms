
    var verifyCallback = function(captcha_response) {
        var url = '/api/validate_recaptcha/'
        var posting = $.post( url, { captcha_response: captcha_response});
        posting.done(function( response ) {
            if(response.result) {
                $('#contact_button').removeAttr("disabled");
                $("#contact_button").removeClass("hide");
                $("#contact_button").show();
            } else {
                alert("Captcha Validation Issue");
            }
        });
    };
    var onloadCallback = function() {
        grecaptcha.render('google_recaptcha', {
            'sitekey' : '6LdhIwMTAAAAALOXVuFBhvUSMrk_J9wM6daQe6Kv',
            'callback' : verifyCallback,
            'theme' : 'light'
        });
    };
