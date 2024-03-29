var url = 'http://arturo.interpegasus.com';
// var url = 'http://127.0.0.1:8000';

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
            $("#ajax_project_content").hide();
            $("#project_content").show();
            if(data.length){
                $.each(data, function(i, record) {
                    $("#gallery_index").append('<li><a href="/en/gallery/'+record.slug+'" onclick="javascript:set_gallery('+ record.id +');">'+ record.name +'</a></li>').show('slow');
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
            $("#ajax_project_content").hide();
            $("#project_content").show();
            if(data.length){
                $.each(data, function(i, record) {
                    $("#page_index").append('<li><a href="javascript:void(0);" onclick="javascript:set_page('+ record.id +');">'+ record.title +'</a></li>').show('slow');
                });
            }else{
                $("#page_index").append('<li>No Data</li>').show('slow');
            }
        }
    });
}

function set_gallery(gallery_id){
    // Show Ajax
    $("#ajax_project_content").show();
    $("#project_content").hide();
    // Get Images in Galery
    set_gallery_images(gallery_id);
    $("#ajax_project_content").hide();
    $("#project_content").show();
    $("#popupProjects").fadeOut("slow");
}

function set_gallery_images(gallery_id){
    request = url + '/ajax/gallery/' + String(gallery_id);
    $.ajax({
        dataType: "json",
        url: request,
        success: function(data) {
            if(data.length){
                $("#image_gallery_container").empty();
                $.each(data, function(i, record) {
                    $("#image_gallery_container").append('' +
                    '<div class="content"><div>' +
                    '<a href="'+ record.picasa_photo_url +'">' +
                    '<img src="'+ record.picasa_thumb_url +'" title="'+ record.name +'" alt="'+ record.name +'" class="thumb" />' +
                    '</a></div></div>').show('slow');
                    load_gallery();
                });
            }else{
                $("#page_index").append('<li>No Data</li>').show('slow');
            }
        }
    });
}


function set_page(page_id){
    request = url + '/ajax/page/' + String(page_id);
    $.ajax({
        dataType: "json",
        url: request,
        success: function(data) {
            var content =  $("#project_content").html();
            $("#project_content").empty();
            if(data){
                $("#project_content").append('<h1>'+ data.title +'</h1>' +'<article">'+ data.content +'</article>').show('slow');
            }else{
                $("#project_content").append('<h3>No Data</h3>').show('slow');
            }
            $("#project_content").append('<div><a href="javascript:void(0);" onclick="javascript:go_back()">Back</a></div>').show('slow');
        }
    });
}

function go_back(){
    $("#project_content").empty();
    $("#project_content").append('<h1>Galleries</h1><ul id="gallery_index"></ul><div class="border"></div><h1>Pages</h1><ul id="page_index"></ul>');
    create_gallery_links();
    create_page_links();
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