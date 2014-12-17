/***************************/
//@Author: Adrian "yEnS" Mato Gondelle
//@website: www.yensdesign.com
//@email: yensamg@gmail.com
//@license: Feel free to use it, but keep this credits please!					
/***************************/
//Projects Page Pop Up
var popupProjectsStatus = 0;

function loadPopupProjects(){
	if(popupProjectsStatus==0){
		$("#popupProjects").fadeIn("slow");
		popupProjectsStatus = 1;
	}
}

function disablePopupProjects(){
	if(popupProjectsStatus==1){
		$("#popupProjects").fadeOut("slow");
		popupProjectsStatus = 0;
	}
}

function centerPopupProjects(){
	var windowWidth = document.documentElement.clientWidth;
	var windowHeight = document.documentElement.clientHeight;
	var popupProjectsHeight = $("#popupProjects").height();
	var popupProjectsWidth = $("#popupProjects").width();
	$("#popupProjects").css({
		"position": "absolute",
		"top": windowHeight/2-popupProjectsHeight/2,
		"left": windowWidth/2-popupProjectsWidth/2
	});
}


$(document).ready(function(){
	$("#popupProjects").fadeOut();
	popupProjectsStatus = 0;
	$("#projects").click(function(){
		$("#popupProjects").css({
			"visibility": "visible"	});
		centerPopupProjects();
		loadPopupProjects();
		$("#popupProjects").mCustomScrollbar("vertical",400,"easeOutCirc",1.05,"auto","yes","yes",10);
	});
	$("#popupProjectsClose").click(function(){
		disablePopupProjects();
	});
	$("#bg").click(function(){
		disablePopupProjects();
	});
	$(document).keyup(function(e){
		if(e.keyCode === 27)
			disablePopupProjects();
	});
});