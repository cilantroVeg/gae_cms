$(document).ready(function() {

	jQuery.validator.addMethod("checkCaptcha", (function() {
		var isCaptchaValid;
		isCaptchaValid = false;
		$.ajax({
			url: "http://127.0.0.1:8080/api/validate_recaptcha",
			type: "POST",
			async: false,
			data: {
				captcha: $("#g-recaptcha-response").val()
			},
			success: function(response) {
				if (response === "true") {
					alert(response)
				} else {
					alert(response)
				}
			}
		});
		return false;
	}), "");

	$("#create_user_form").validate({
		rules : {
			email : {
				email : true,
				required : true
			},
			confirm_email : {
				email : true,
				required : true,
				equalTo : "#email"
			},
			password : {
				required : true,
				minlength : 7
			},
			confirm_password : {
				required : true,
				minlength : 7,
				equalTo : "#password"
			}
		}
	});

	$("#contact_form").validate({
		rules : {
			contact_email : {
				email : true,
				required : true
			},
			contact_name : {
				required : true,
				minlength : 7
			},
			contact_comment : {
				required : true,
				minlength : 21
			},
			captcha: {
				required: true,
				checkCaptcha: true
			}
		},
		messages: {
			captcha: {
				checkCaptcha: "Your Captcha response was incorrect. Please try again."
			}
		}
	});

	$("#login_user_form").validate({
		rules : {
			email_2 : {
				email : true,
				required : true
			},
			password_2 : {
				required : true,
				minlength : 7
			}
		}
	});
	$('#code').change(function() {
		$('#code_1').val($('#code').val());
		$('#code_2').val($('#code').val());
	});
});