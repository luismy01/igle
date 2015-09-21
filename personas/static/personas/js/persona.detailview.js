app.PersonaDetailView = Backbone.View.extend({

	template: _.template( $("#persona-detail-template").html() ),

	initialize: function (options) {
		this.router = options.router;
	},

	render: function () {

		var html = this.template(this.model.attributes);
		this.$el.html( html );

		this.$habilitar = this.$(".btn-habilitar");
        this.$dialog = this.$("#dialogo-eliminar");

		return this;
	},

	events: {
		"click .btn-editar": "editar",
		"click .btn-habilitar": "habilitar",
		"click .btn-eliminar": "onEliminar",
        "click .btn-eliminar-ok": "eliminar",
	},

    habilitar: function(evt) {

    	var hasButtonPressed = this.$habilitar.attr("aria-pressed") == "true" ? true : false;
    	var text = hasButtonPressed == true ? "Deshabilitar" : "Deshabilitado";
    	this.$habilitar.text(text);
    	
    	this.model.set({habilitado: hasButtonPressed});
    	this.model.save();

    	this.$habilitar.blur();
    	
    },

    editar: function (evt) {
    	// evento manejado por el router
    },

    onEliminar: function(evt) {
    	
    	var compile = _.template( $("#dialogo-eliminar-template").html() );
    	var html = compile( {persona: this.model} );

    	this.$dialog.html( html );
    	this.$dialog.modal( "show" );

    },

    eliminar: function (evt) {

        var that = this;

        this.model.destroy({wait:true});

        this.$dialog.on("hidden.bs.modal", function(evt){
            that.trigger("delete");
        });

        this.$dialog.modal( "hide" );

    }

});