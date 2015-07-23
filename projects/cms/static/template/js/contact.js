$(document).ready(function(){
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