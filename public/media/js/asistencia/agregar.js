
$("#form-asist .numeric").keypress( function (evt) {
	if (evt.which < 48 || evt > 57) evt.preventDefault();
});

$("#save").click( function (evt) {
	
	$("#form-asist").submit();

});