app.PersonaListView = Backbone.View.extend({

	template: _.template( $("#persona-list-template").html() ),

	initialize: function () {
		this.listenTo(this.collection, "add", this.render);
		this.listenTo(this.collection, "destroy", this.render);
		this.listenTo(this.collection, "reset", this.render);
	},

	render: function () {

		var html = this.template({personas: this.collection.models});
		this.$el.html( html );

		return this;
	},

	events: {
		"keyup div#filtros .nombre": "filtrar",
		"keyup div#filtros .email": "filtrar",
		"keyup div#filtros .congregacion": "filtrar",
		"click div#filtros .genero": "filtrar",
	},

	filtrar: function(evt) {

		var nombre = this.$("div#filtros .nombre").val().toLowerCase();
		var email = this.$("div#filtros .email").val().toLowerCase();
		var congregacion = this.$("div#filtros .congregacion").val().toLowerCase();

		var personas = this.collection.filter(function(persona){
			var predicate = persona.get("nombre").toLowerCase().contains(nombre)
				&& persona.get("email").toLowerCase().contains(email)
				&& persona.get("congregacion").toLowerCase().contains(congregacion);
			return predicate;
		});

		var compile_template = _.template( $("#persona-list-list-group-template").html() );
		var html = compile_template({personas: personas});

		this.$("#list-group").html(html);
	},

});