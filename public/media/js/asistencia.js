
$(function () {

	/* idioma por defecto para moment */
	moment.lang("es");

	$('#tabs a').click(function (e) {
	  e.preventDefault();
	  $(this).tab('show');
	});

});