var url = 'http://arturo.interpegasus.com';
var url = 'http://127.0.0.1:8000';

$(document).ready(function() {
    create_gallery_links();
    create_page_links();
});


function create_gallery_links(){
    request = url + '/ajax/galleries/';
    $.ajax({
        dataType: "json",
        url: request,
        success: function(data) {
            if(data.length){
                $.each(data, function(i, record) {
                    $("#gallery_index").append('<li><a href="gallery_1">'+ record.name +'</a></li>').show('slow');
                });
            }else{
                $("#gallery_index").append('<li>No Data</li>').show('slow');
            }
        }
    });
}

function create_page_links(){
    request = url + '/ajax/pages/';
    $.ajax({
        dataType: "json",
        url: request,
        success: function(data) {
            if(data.length){
                $.each(data, function(i, record) {
                    $("#page_index").append('<li><a href="gallery_1">'+ record.title +'</a></li>').show('slow');
                });
            }else{
                $("#page_index").append('<li>No Data</li>').show('slow');
            }
        }
    });
}

function set_images(){

}

function preload_images(){
    	$(window).load(function() {
			var imageArray = ['images/gallery/2.jpg', 'images/gallery/3.jpg', 'images/gallery/4.jpg', 'images/gallery/5.jpg', 'images/gallery/6.jpg'];
			var hidden = $('body').append('<div id="img-cache" style="display:none/>').children('#img-cache');
			$.each(imageArray, function (i, val) {
			  $('<img/>').attr('src', val).appendTo(hidden);
			});
	});
}