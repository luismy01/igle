var updateView = new PersonaEditView();

$("#personaForm").validate({
	
	debug: true,

	invalidHandler: function(event, validator) {
		console.log("formulario invalido")
	},

	rules: {
		celular: {
			required: true
		}
	}

});