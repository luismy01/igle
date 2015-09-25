var updateView = new PersonaEditView();

$("#personaForm").validate({
	
	debug: true,

	errorClass: "has-error",

	highlight: function(element, errorClass, validClass) {
		var formGroup = $(element).parent().parent();
		formGroup.addClass(errorClass).removeClass(validClass);
	},

	unhighlight: function(element, errorClass, validClass) {
		var formGroup = $(element).parent().parent();
		formGroup.removeClass(errorClass);
	},

	invalidHandler: function(event, validator) {
		console.log("formulario invalido")
	},

	rules: {
		celular: {
			required: true,
			digits: true,
		}
	},

});