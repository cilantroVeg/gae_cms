$(document).ready(function(){

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
			}
		}
	});



});